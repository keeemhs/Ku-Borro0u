# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', #1
#         'NAME': 'borro0u_db', #2
#         'USER': 'root', #3                      
#         'PASSWORD': '0000',  #4              
#         'HOST': 'localhost',   #5                
#         'PORT': '3306', #6
#     }
# }
# SECRET_KEY = 'django-insecure-5o%$iqvg9com^5rak@*n^k6v!(0rs#c22^3h=am5lj$+buj&ys'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', #1
#         'NAME': 'heroku_c81f4c5688d89d7', #2
#         'USER': 'b8f7e9653ddc36', #3                      
#         'PASSWORD': '1b4bfcb9',  #4              
#         'HOST': 'us-cdbr-east-06.cleardb.net',   #5                
#         'PORT': '3306', #6
#         # 'OPTIONS': {
#         #     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         #     'charset': 'utf8mb4',
#         #     'use_unicode': True,
#         # },
#         # 'CONN_MAX_AGE': 5,
#     }
# }
# SECRET_KEY = 'django-insecure-5o%$iqvg9com^5rak@*n^k6v!(0rs#c22^3h=am5lj$+buj&ys'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'kxw0mv1b4ez2w3e9', #2
        'USER': 'pvmpid9t70k4l4b4', #3                      
        'PASSWORD': 'l48y09x1mo5dvphn',  #4              
        'HOST': 'qvti2nukhfiig51b.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',   #5                
        'PORT': '3306', #6
        'OPTIONS': {
        'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}
SECRET_KEY = 'django-insecure-5o%$iqvg9com^5rak@*n^k6v!(0rs#c22^3h=am5lj$+buj&ys'
