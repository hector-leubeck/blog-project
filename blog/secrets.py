AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
     },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
     },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
     },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
     },
]


DATABASES = {'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'newdb',
    'HOST': '127.0.0.1',
    'PORT': '3306',
    'USER': 'hector',
    'PASSWORD': 'h2ct4r'}}
