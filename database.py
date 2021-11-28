SECRET_KEY = "1a6c75e61de6b04fe76788ce0febe04781e01ce87564371739afba8877e09546"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$6JBNZ/XaR/RTVvWxvLWYNOK6gbMT686m6kG7BykkZ6OZXZGRn42G2",
        "disabled": False,
    }
}