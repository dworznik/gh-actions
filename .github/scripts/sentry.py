import sentry_sdk
import os
import sys

SENTRY_DSN = os.getenv("SENTRY_DSN")
print(SENTRY_DSN)

sentry_sdk.init(
    dsn=SENTRY_DSN,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

def divide(a, b):
    return a / b

if __name__ == "__main__":
    print(SENTRY_DSN)
    result = divide(2, 0)
