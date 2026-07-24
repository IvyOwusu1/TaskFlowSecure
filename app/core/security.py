from passlib.context import CryptContext

# --------------------------------------------------------------------------
# Password hashing context
# --------------------------------------------------------------------------
# CryptContext is passlib's configurable hashing manager. We tell it to use
# bcrypt as the only scheme. bcrypt is deliberately slow and includes a
# built-in random salt per hash, which is exactly what you want for
# passwords: it makes brute-force and rainbow-table attacks impractical,
# even if your database is ever leaked.
#
# deprecated="auto" means that if this scheme list changes in the future
# (e.g. you migrate to argon2), passlib can automatically detect and flag
# hashes created with an older, now-deprecated scheme -- without you having
# to write that migration logic by hand.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Hash a plaintext password for storage.

    Passwords must never be stored in plaintext or with reversible
    encryption. If a database is ever compromised, plaintext or encrypted
    passwords hand attackers immediate access to every user's account
    (and, since people reuse passwords, often their accounts on other
    sites too). Hashing is one-way: there is no function that turns a
    hash back into the original password.

    The returned string encodes the algorithm, a random salt, and the
    hash itself -- everything needed to verify a future login attempt,
    with no need to store the salt separately.
    """
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify a plaintext password attempt against a stored hash.

    Because hashing is one-way, you can't "decrypt" hashed_password to
    compare it directly. Instead, this re-hashes the incoming plaintext
    password using the same algorithm and salt embedded in
    hashed_password, then compares the two hashes. passlib handles this
    salt extraction and comparison internally, and does so using a
    constant-time comparison to avoid leaking timing information that
    could otherwise help an attacker guess the password character by
    character.
    """
    return pwd_context.verify(password, hashed_password)