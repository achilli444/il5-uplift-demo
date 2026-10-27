from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app, raise_server_exceptions=False)


def test_healthz():
    assert client.get("/healthz").json() == {"ok": True}


def test_login_and_asset():
    tok = client.post("/login", params={"username": "operator", "password": "Password1"}).json()["token"]
    r = client.get("/assets/C-130J-01", headers={"Authorization": f"Bearer {tok}"})
    assert r.status_code == 200 and r.json()["status"] == "FMC"


def test_bad_login():
    assert client.post("/login", params={"username": "operator", "password": "nope"}).status_code == 401
