"""
wizcli test app with lots of obvious fake secrets.
ALL SECRETS BELOW ARE FAKE / TEST-ONLY.  DO NOT USE IN PRODUCTION.
They are intentionally obvious so secret scanners trigger reliably.
"""

import os
import base64
import json

# ------------------------
# OBVIOUS FAKE HARD-CODED SECRETS
# ------------------------
# (clearly labeled with FAKE/TEST/DO_NOT_USE)
AWS_ACCESS_KEY_ID = "AKIA-FAKE-TEST-ACCESSKEY-DO_NOT_USE"
AWS_SECRET_ACCESS_KEY = "FAKEawsSecretKey_DO_NOT_USE_1234567890"
GCP_SERVICE_ACCOUNT_KEY = "gcp-service-account-FAKE-TEST-key-000000"
AZURE_CLIENT_ID = "azure-client-id-FAKE-0000"
AZURE_CLIENT_SECRET = "azure-client-secret-FAKE-DO-NOT-USE"

DATABASE_PASSWORD = "DB_PASSWORD_FAKE_TEST_ChangeMe!"
DATABASE_URL = "postgresql://test_user:DB_PASSWORD_FAKE_TEST_ChangeMe!@localhost:5432/testdb"

STRIPE_API_KEY = "sk_test_FAKE_STRIPE_KEY_123456"
SLACK_WEBHOOK = "https://hooks.slack.com/services/FAKE/TEST/WEBHOOK"
SENTRY_DSN = "https://public:private@o0.ingest.sentry.io/0-FAKE"

JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.FAKE_PAYLOAD.SIGNATURE_DO_NOT_USE"
OAUTH_CLIENT_SECRET = "OAUTH_CLIENT_SECRET_FAKE_TEST_0000"

# ------------------------
# ENV VAR fallback pattern (simulate secrets passed via env)
# ------------------------
# Use environment variable if set, otherwise fall back to an obvious fake secret.
PAYMENT_SERVICE_TOKEN = os.environ.get("PAYMENT_SERVICE_TOKEN", "PAYMENT_TOKEN_FAKE_DO_NOT_USE")
EXTERNAL_API_KEY = os.environ.get("EXTERNAL_API_KEY", "EXT_API_KEY_FAKE_TEST_ABC")

# ------------------------
# BASE64 / HEX / ENCODED secrets
# ------------------------
BASE64_SECRET = base64.b64encode(b"base64-secret-value-TEST").decode("ascii")  # encoded at runtime
HEX_SECRET = "deadbeefcafebabefake000000000TEST"

# ------------------------
# MULTI-LINE/PEM / PRIVATE KEY (FAKE)
# ------------------------
FAKE_RSA_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAwFAKEKEY-DO-NOT-USE-TEST-0000
FAKE-THIS-IS-NOT-A-REAL-KEY-AND-IS-FOR-TESTING-ONLY
EXTRA-LINES-TO-MAKE-IT-LOOK-LIKE-A-PEM-KEY-FAKE
-----END RSA PRIVATE KEY-----"""

FAKE_SSH_PRIVATE_KEY = """-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktFAKE-DO-NOT-USE-TEST-0000
FAKE-SSH-KEY-THIS-IS-A-TEST-ONLY
-----END OPENSSH PRIVATE KEY-----"""

# ------------------------
# KUBERNETES / DOCKER secrets
# ------------------------
K8S_SECRET_BASE64 = "dGVzdC1rOHMtc2VjcmV0LXRlc3Q="  # "test-k8s-secret-test"
DOCKERFILE_ENV_SECRET = "DOCKER_SECRET_FAKE_123456"

# ------------------------
# CONFIG/BLOB examples
# ------------------------
CONFIG_JSON = {
    "service": {
        "api_key": "CONFIG_API_KEY_FAKE_000111",
        "db_password": "CONFIG_DB_PASS_FAKE_DO_NOT_USE"
    }
}

# ------------------------
# SECRET IN A COMMENT (simulating leftover)
# ------------------------
# NOTE: TEMP ADMIN PWD = tmpAdminPwd-TEST-DO-NOT-USE-98765

# ------------------------
# COOKIE / SESSION / CSRF
# ------------------------
SESSION_COOKIE = "session=FAKESESSIONCOOKIE12345; HttpOnly"
CSRF_TOKEN = "csrf-token-FAKE-TEST-abcdef"

# ------------------------
# Helper / usage (prints everything so scanners that look at logs also trigger)
# ------------------------
def print_header():
    print("\n" + "#" * 80)
    print("#  WIZCLI TEST APP — OBVIOUS FAKE SECRETS (FOR TESTING ONLY)  ")
    print("#  ALL VALUES BELOW ARE FAKE / DO NOT USE IN REAL SYSTEMS  ")
    print("#" * 80 + "\n")

def show_hardcoded_secrets():
    print("AWS_ACCESS_KEY_ID:", AWS_ACCESS_KEY_ID)
    print("AWS_SECRET_ACCESS_KEY:", AWS_SECRET_ACCESS_KEY)
    print("GCP_SERVICE_ACCOUNT_KEY:", GCP_SERVICE_ACCOUNT_KEY)
    print("AZURE_CLIENT_ID:", AZURE_CLIENT_ID)
    print("AZURE_CLIENT_SECRET:", AZURE_CLIENT_SECRET)
    print("DATABASE_URL:", DATABASE_URL)
    print("DATABASE_PASSWORD:", DATABASE_PASSWORD)
    print("STRIPE_API_KEY:", STRIPE_API_KEY)
    print("SLACK_WEBHOOK:", SLACK_WEBHOOK)
    print("SENTRY_DSN:", SENTRY_DSN)
    print("JWT_TOKEN (truncated):", JWT_TOKEN[:60] + "...")
    print("OAUTH_CLIENT_SECRET:", OAUTH_CL_
