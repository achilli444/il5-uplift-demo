"""Mission Readiness Tracker - tiny FastAPI service used for the IL2->IL5 uplift demo.

Planted gaps (do not fix here; the uplift PRs fix them):
  G1 MD5 password hashing            (IA-5(1), SC-13, ASD STIG password storage)      -> auth.hash_password
  G2 Hardcoded API key                (IA-5(7), CWE-798)                               -> settings.API_KEY
  G3 No idle session timeout         (AC-11/AC-12, ASD STIG 15-min idle)              -> auth.issue_token
  G4 SQL built by string concat      (SI-10, CWE-89)                                   -> db.find_asset
  G5 Stack trace returned to client  (SI-11, CWE-209)                                  -> main.debug_exception_handler
  G6 No DoD consent banner           (AC-8)                                            -> GET /login has no banner
  G7 Audit log missing who/where     (AU-3, AU-12)                                     -> main.audit
  G8 Privileged pod, latest tag, secret in env (K8s STIG, CM-5(6), SR-3)              -> k8s/deployment.yaml
"""
import logging
import traceback

from fastapi import FastAPI, Depends, HTTPException, Request, Header
from fastapi.responses import JSONResponse, PlainTextResponse

from . import auth, db, settings

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("mrt")

app = FastAPI(title="Mission Readiness Tracker", version="0.1.0")


def audit(event: str, detail: str) -> None:
    # G7: no actor, source address, outcome or UTC timestamp
    log.info("AUDIT %s %s", event, detail)


@app.exception_handler(Exception)
async def debug_exception_handler(request: Request, exc: Exception):
    # G5: internals leak to the client
    return JSONResponse(status_code=500, content={"error": str(exc), "trace": traceback.format_exc()})


@app.get("/login", response_class=PlainTextResponse)
def login_page():
    # G6: no DoD Notice and Consent Banner before authentication
    return "POST username/password to /login"


@app.post("/login")
def login(username: str, password: str):
    user = db.get_user(username)
    if not user or user["password_hash"] != auth.hash_password(password):
        audit("login_failed", username)
        raise HTTPException(status_code=401, detail="bad credentials")
    token = auth.issue_token(username)
    audit("login_ok", username)
    return {"token": token}


def require_token(authorization: str = Header(default="")):
    claims = auth.verify_token(authorization.replace("Bearer ", ""))
    if not claims:
        raise HTTPException(status_code=401, detail="invalid token")
    return claims


@app.get("/assets/{name}")
def get_asset(name: str, claims=Depends(require_token)):
    row = db.find_asset(name)
    if not row:
        raise HTTPException(status_code=404, detail="no such asset")
    audit("asset_read", name)
    return row


@app.get("/export")
def export(x_api_key: str = Header(default="")):
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="forbidden")
    return {"assets": db.all_assets()}


@app.get("/healthz")
def healthz():
    return {"ok": True}
