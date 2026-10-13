# Django REST Framework Watchlist API

A Django REST Framework API for managing streaming platforms, watchlists, and user reviews. It also provides user registration and JWT authentication.

## Requirements

- Python 3.10 or later
- Django
- Django REST Framework
- Django REST Framework Simple JWT

## Setup

Run these commands from the workspace root in PowerShell:

```powershell
cd .\DRF
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install Django djangorestframework djangorestframework-simplejwt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The development server is available at `http://127.0.0.1:8000/`.

## API routes

| Method | Route | Description |
| --- | --- | --- |
| `POST` | `/accounts/register/` | Register a user; returns access and refresh JWTs |
| `POST` | `/accounts/api/token/` | Obtain a JWT pair with username and password |
| `POST` | `/accounts/api/token/refresh/` | Refresh an access token |
| `POST` | `/accounts/logout/` | Log out using a token-authentication token |
| `GET` | `/watch/list/` | List watchlist entries |
| `POST` | `/watch/list/` | Create a watchlist entry (admin only) |
| `GET`, `PUT`, `DELETE` | `/watch/<id>/` | Retrieve, update, or delete a watchlist entry |
| `GET` | `/watch/stream/` | List streaming platforms |
| `POST` | `/watch/stream/` | Create a streaming platform (admin only) |
| `GET`, `PUT`, `DELETE` | `/watch/stream/<id>/` | Retrieve, update, or delete a streaming platform |
| `POST` | `/watch/<id>/review-create/` | Add a review (authenticated users) |
| `GET` | `/watch/<id>/review/` | List reviews for a watchlist entry (authenticated users) |
| `GET`, `PUT`, `DELETE` | `/watch/review/<id>/` | Retrieve a review; only its author or a staff user can modify or delete it |
| `GET`, `POST` | `/api-auth/login/` | DRF browsable API login |
| `GET`, `POST` | `/api-auth/logout/` | DRF browsable API logout |
| — | `/admin/` | Django admin site |

For JWT-protected endpoints, send the access token in the request header:

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Development notes

- The project uses SQLite. Run `python manage.py migrate` after pulling model or migration changes.
- Watchlist and review endpoints use pagination configured in Django REST Framework.
- The checked-in development settings enable `DEBUG` and contain a development secret key. Configure secure environment-specific settings before deploying; do not use these development settings in production.
- Run the available tests with `python manage.py test`.
