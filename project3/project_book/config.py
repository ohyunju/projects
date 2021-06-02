class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# class DevelopmentConfig(Config):
#     DEBUG = True
#     #SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///dev_db.sqlite3'

#     database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
#         dbuser="myouhuaw",
#         dbpass="xZ2QnNpBkG4bX1KBk6mxmxGXT8MAYick",
#         dbhost="salt.db.elephantsql.com",
#         dbname="myouhuaw"
#     )
#     SQLALCHEMY_DATABASE_URI=database_uri

# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///prod_db.sqlite3'
