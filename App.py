import os
import base64
import yaml

# ---------- Hard-coded (fake) secrets ----------
API_KEY = "TEST_API_KEY_ABC1234567890_FAKE"
DB_PASSWORD = "P@ssw0rdFakeForTesting!"
OAUTH_TOKEN = "ya29.FAKE_OAUTH_TOKEN_9876543210"

def print_secrets():
    print("Hard-coded API_KEY:", API_KEY)            # should be flagged
    print("Hard-coded DB_PASSWORD:", DB_PASSWORD)    # should be flagged

# ---------- Load from .env fallback pattern ----------
# (simulate using environment variables; if not set, fallback to a hardcoded default)
EXTERNAL_SERVICE_TOKEN = os.environ.get("EXTERNAL_SERVICE_TOKEN", "ext-token-default-TEST-0001")
print("External service token (env/default):", EXTERNAL_SERVICE_TOKEN)

# ---------- Read config file containing secrets ----------
def read_config_secret(path="config.yaml"):
    try:
        with open(path, "r") as f:
            cfg = yaml.safe_load(f)
            if cfg and "service" in cfg:
                print("Config file secret api_key:", cfg["service"].get("api_key"))
    except Exception as e:
        print("Could not read config.yaml:", e)

# ---------- Base64-encoded secret in code ----------
BASE64_SECRET = "c2VjcmV0LWJhc2U2NC10b2tlbi1URVNULQ=="  # "secret-base64-token-TEST-"
def decode_base64_secret():
    decoded = base64.b64decode(BASE64_SECRET).decode("utf-8")
    print("Decoded base64 secret:", decoded)

# ---------- Secret in comment (simulating leftovers) ----------
# TODO: temporary admin password tmpAdminPass98765

if __name__ == "__main__":
    print("Starting test app with fake secrets.")
    print_secrets()
    read_config_secret()
    decode_base64_secret()
