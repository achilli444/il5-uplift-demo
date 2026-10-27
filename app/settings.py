import os

# G2: hardcoded credential checked into source
API_KEY = "mrt-export-7f3a9c2e1b4d5a6f8e9d0c1b2a3f4e5d"
TOKEN_SECRET = os.environ.get("TOKEN_SECRET", "change-me")
SESSION_IDLE_MINUTES = None  # G3: unset -> no timeout
