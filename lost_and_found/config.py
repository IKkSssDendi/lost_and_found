class DevConfig():
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wheneverhwp123@localhost/gxgk'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    DEBUG = True
    REDIS_URL = "redis://:@localhost:6379/0"

    TOKEN = 'LostAndFound'
    appID = ''
    appSerect = ''
    BASE_ACCESS_TOKEN_URL = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=%s&appid=%s&secret=%s'
    CODE_URL = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=%s&state=%s#wechat_redirect'
    ACCESS_TOKEN_URL = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code'
    GET_USER_DATA_URL = 'https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=%s'