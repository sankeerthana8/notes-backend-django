# notes_backend/settings.py

INSTALLED_APPS = [
    # Other apps
    'notes',
]

# Database configuration (SQLite in this case)
# Ensure your DATABASES setting looks like this:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
