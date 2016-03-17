
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://taewookim:1234@173.194.86.171:3306/roompi2_db"
    SQLALCHEMY_TRACK_MODIFICATION = True
    @classmethod
    def init_app(cls, app):
        # config setting for flask app instance
        app.config.from_object(cls)
        return app

