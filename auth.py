import bcrypt

MAX_LOGIN_ATTEMPTS = 5


def verify_password(password, password_hash):
    return bcrypt.checkpw(password, password_hash)


def login_user(username, password):
    user = find_user(username)

    if verify_password(password, user.password_hash):
        return create_session(user)

    return None


def logout_user(user):
    delete_session(user)