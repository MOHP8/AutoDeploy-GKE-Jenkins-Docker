import os

class Config:
    SECRET_KEY = '34ba6c62bb02838b4eda7729ba848db5'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

    # 新增以下部分
    MAIL_SERVER = 'smtp.gmail.com'  # Google 的 SMTP 伺服器
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'pphao481@gmail.com'  # 使用你的 Gmail 信箱
    MAIL_PASSWORD = 'fbie eszx xtdm qvwl'  # 使用你的 Gmail 密碼
    MAIL_DEFAULT_SENDER = 'pphao481@gmail.com'
    MAIL_TOKEN_EXPIRATION = 300  # 令牌過期時間（秒）

    #Google
    GOOGLE_CLIENT_ID = '565481039292-kfilnia3d2513brdmgakmhdrtp8os9j1.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = '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'

    # Facebook
    FACEBOOK_APP_ID = '1373670063519081'
    FACEBOOK_SDK_VERSION = 'v18.0'

    # reCAPTCHA (v2)
    SITE_KEY_V2 = '6LdHqRYpAAAAADcHoeh7VyxTpg3srs-daO1wtxlb'
    SECRET_KEY_V2 ='6LdHqRYpAAAAAMqTDeBK_woTEAgTOj-Gf3xTxlmL'

    #reCAPTCHA (v3)
    SITE_KEY_V3 = '6LcTqxYpAAAAANLG3VmQb50zA4NThRYswqp3FaaY'
    SECRET_KEY_V3 ='6LcTqxYpAAAAAEe200811McpdjqYrclcF8-68iVc'

    # twitter
    TWITTER_CLIENT_ID='L6hd0MYy5jhB0rzHAXyo5OqLX',
    TWITTER_CLIENT_SECRET='4m4evpLe2oIdHmoDUVvdYZv9YgkuHziLPKfXxqYt6auX5DO6cO',

    #ECPay
    # 測試環境
    EC_PAY_API_BASE_URL = 'https://payment-stage.ecpay.com.tw/Cashier/AioCheckOut/V5'
    # 正式環境
    # EC_PAY_API_BASE_URL = 'https://payment.ecpay.com.tw/Cashier/AioCheckOut/V5'
    EC_PAY_MERCHANT_ID = '3002607'
    EC_PAY_HASH_KEY = 'pwFHCqoQZGmho4w6'
    EC_PAY_HASH_IV = 'EkRm7iFT261dpevs'

    #google_ai_api_key
    GOOGLE_AI_API_KEY = 'AIzaSyAifoDo7y8XcEMREhFYUNL5yrUwVsrBvKU'

    #Mysql(database)
    MySQL_host = 'mysql'
    MySQL_user = 'docker_user'
    MySQL_password = '1234'
    MySQL_database = 'telecomsquare'

    # #Mysql(database)
    # MySQL_host = '127.0.0.1'
    # MySQL_user = 'root'
    # MySQL_password = 'b3799126'
    # MySQL_database = 'telecomsquare'