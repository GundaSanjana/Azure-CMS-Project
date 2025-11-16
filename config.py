import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '43e28e10-e1ba-4785-a09c-797c8f147c77'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'images11'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'wC7bweFhSgEfey9JeK9xsVO4fryQLm2x/nyZyIW6u+SqY9OM7lsU1kiLDS7aCa4B/RLuIm/2TSF4+ASt+XFgDg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms22.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'CMS4dmin'

    # Corrected SQLAlchemy URI (username:password@server:1433/db?driver=...)
    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://'
        + SQL_USER_NAME + ':' + SQL_PASSWORD
        + '@' + SQL_SERVER + ':1433/'
        + SQL_DATABASE
        + '?driver=ODBC+Driver+17+for+SQL+Server'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'dIO8Q~cJypiPEn2W~nhG1hPt91GqBc7cm-kYwbH'
    AUTHORITY = os.environ.get('AUTHORITY') or "https://login.microsoftonline.com/common"
    CLIENT_ID = os.environ.get('CLIENT_ID') or 'ce983c51-5ef0-4cb2-838f-f9618aee6f57'

    # MUST start with a slash:
    REDIRECT_PATH = "/getAToken"

    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"
