![workflow](https://github.com/raphiniert/fastapi-vue/actions/workflows/test.yml/badge.svg)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![code style](https://img.shields.io/badge/code%20style-black-000000.svg)


# fastapi-vue
fastapi, elasticsearch and vue

## Project structure
    .
    ├── backend                  # fastapi app
    │   ├── api                  # api
    │   │   ├── core             # config
    │   │   ├── crud             # crud functions
    │   │   ├── db               # db setup and models
    │   │   ├── routers          # actual endpoints
    │   │   ├── main.py          # main entrypoint
    │   │   └── schemas.py       # demo json api schemas
    │   ├── tests                # tests
    │   │   └── conftest.py      # fixtures
    │   ├── Dockerfile           # python3.10-alpine, running api main.py
    │   ├── requirements-dev.txt # list of version pinned dev dependencies
    │   └── requirements.txt     # list of version pinned python dependencies
    ├── .env                     # environment variables
    ├── .gitignore               # .gitignore file
    ├── .pre-commit-config.yml   # pre commit config
    ├── compose.yaml             # docker compose file
    └── README.md                # this readme file


## Setup

### Clone repo
```shell script
git clone https://github.com/raphiniert/fastapi-vue.git
cd fastapi-vue
```

#### Local developement

Create a `.env` file with the following content:

```text
# backend
PROJECT_NAME=demo

# Postgres
POSTGRES_SERVER=db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=fastapi-vue-pg-password
POSTGRES_DB=fastapi-demo
POSTGRES_PORT=5432

# Timezone
TZ=Europe/Vienna
```

and run docker compose:

```shell script
docker compose up -d
```

**[Optional] Install dev dependencies**

```shell script
. venv/bin/activate
pip install -r backend/requirements-dev.txt  # includes requirements.txt
```

## Testing

### API Backend Tests

```shell script
docker compose backend coverage run -m pytest
```
