import os 
from pathlib import Path
from django.urls import reverse_lazy
from django.templatetags.static import static


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-zc7@lc#$&jw_c%-h_f05pj2b!ty+)vydc5z5r)1wuk_%0z00_e'


DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    'unfold',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Client',
    'rest_framework', 
    'drf_spectacular',
    'drf_spectacular_sidecar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ElevatorProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ElevatorProject.wsgi.application'


SPECTACULAR_SETTINGS = {
    'TITLE': 'Centreg',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR', 
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
}


REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


UNFOLD = {
    "SITE_TITLE": "Centreg",
    "SITE_HEADER": "Centreg",
    "SITE_URL": "/",
    "SITE_ICON": lambda request: static("unfold/images/centreg.png"),
    "SITE_LOGO": lambda request: static("unfold/images/centreg.png"),
    "SITE_SYMBOL": "speed",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "THEME": None,
    "LOGIN": {
        "redirect_after": lambda request: reverse_lazy("admin:index"),
    },
    "SIDEBAR": {
        "show_search": False,
        "show_all_applications": False,
        "navigation": [
            {
                "items": [
                    {
                        "title": "Главная страница",
                        "icon": "home",
                        "link": reverse_lazy("admin:index"),
                    },
                    {
                        "title": "Пользователи",
                        "icon": "people",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                    {
                        "title": "Группы",
                        "icon": "workspaces",
                        "link": reverse_lazy("admin:Client_group_changelist"),
                    },
                    {
                        "title": "Лифты",
                        "icon": "elevator",
                        "link": reverse_lazy("admin:Client_elevator_changelist"),
                    },
                    {
                        "title": "Реклама",
                        "icon": "featured_video",
                        "link": reverse_lazy("admin:Client_advertisement_changelist"),
                    },
                ]
            },
        ],
    },
}

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = 'media/'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'