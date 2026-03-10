# Wedding Invitation Django App

A Django application for wedding invitations.

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Deployment to Render

This app is configured for deployment on Render.com.

### Prerequisites
- A Render account
- Git repository pushed to GitHub/GitLab

### Deployment Steps

1. **Connect Repository**: Connect your Git repository to Render
2. **Create Web Service**: Choose "Web Service" from the dashboard
3. **Configure Build & Deploy**:
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn wedding_invitation.wsgi:application --bind 0.0.0.0:$PORT`
4. **Environment Variables**: Set the following in Render dashboard:
   - `SECRET_KEY`: A secure random string
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: Your Render app URL (e.g., `your-app.onrender.com`)

### Files for Deployment
- `requirements.txt`: Python dependencies
- `build.sh`: Build script for static files
- `Procfile`: Process definition for Render
- `runtime.txt`: Python version specification

## Database

Currently uses SQLite. For production, consider switching to PostgreSQL by updating `settings.py` and setting `DATABASE_URL` environment variable.