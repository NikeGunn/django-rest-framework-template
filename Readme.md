# 🚀 Django REST Framework Quickstart Template

<div align="center">

![Django](https://img.shields.io/badge/Django-5.x-green.svg)
![DRF](https://img.shields.io/badge/DRF-latest-red.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-latest-blue.svg)
![Docker](https://img.shields.io/badge/Docker-ready-blue.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

*A production-ready API template with Django REST Framework, PostgreSQL, and Docker*

</div>

## ✨ Features

- **Django 5.x** - Latest Python web framework
- **Django REST Framework** - Powerful API toolkit
- **PostgreSQL** - Production-grade database
- **Docker & Docker Compose** - Containerization for easy deployment
- **Environment-based Configuration** - Secure settings management
- **Pre-configured API Endpoints** - Ready to extend

## 📦 Tech Stack

| Technology | Purpose |
|------------|---------|
| ![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python) | Core Language |
| ![Django](https://img.shields.io/badge/Django-5.x-green?style=flat-square&logo=django) | Web Framework |
| ![DRF](https://img.shields.io/badge/DRF-Latest-red?style=flat-square&logo=django) | API Framework |
| ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Latest-blue?style=flat-square&logo=postgresql) | Database |
| ![Docker](https://img.shields.io/badge/Docker-Latest-blue?style=flat-square&logo=docker) | Containerization |

## 📂 Project Structure

```
├── api/                  # Django app (Books API)
├── project/              # Django project settings
├── Dockerfile            # Docker image setup
├── docker-compose.yml    # Multi-container setup
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/drf-quickstart-template.git
cd drf-quickstart-template
```

### 2. Configure Environment Variables

Create a `.env` file in the project root:

```ini
POSTGRES_DB=yourdbname
POSTGRES_USER=yourdbuser
POSTGRES_PASSWORD=yourdbpassword
DJANGO_SECRET_KEY=your-django-secret-key
DEBUG=True
```

### 3. Build and Launch

```bash
docker-compose up --build
```

## 🚀 Usage

Once running, your API is available at: `http://localhost:8000/api/books/`

### Example API Request

```bash
curl http://localhost:8000/api/books/
```

## 🛠️ Development Commands

| Command | Description |
|---------|-------------|
| `docker-compose up --build` | Build and start all services |
| `docker-compose down` | Stop and remove containers |
| `docker-compose exec web python manage.py migrate` | Run migrations |
| `docker-compose exec web python manage.py createsuperuser` | Create admin user |

## 🧪 First-Time Setup

After initial deployment, run migrations:

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

Access Django admin at: `http://localhost:8000/admin/`

## 🔌 Port Mappings

- **Django application**: 8000
- **PostgreSQL database**: 5432

## 📝 API Specification

### Book Model

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Auto-generated ID |
| title | String | Book title |
| author | String | Book author |
| published_date | Date | Publication date |

### Sample Response

```json
[
  {
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_date": "1925-04-10"
  }
]
```

## 📄 License

This project is available under the [MIT License](LICENSE).

## 🙌 Acknowledgments

- Inspired by production Django REST Framework projects
- Built for developers who want rapid API development
- Designed with scalability in mind

<div align="center">
<p>Made with ❤️ for the developer community</p>
</div>
