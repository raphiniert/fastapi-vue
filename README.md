# fastapi-vue
fastapi, elasticsearch and vue

## Project structure
    .
    ├── backend                 # fastapi app
    │   ├── api                 # fast
    │   │   └── main.py         # demo json api
    │   ├── Dockerfile          # python3.10-alpine, running api main
    │   └── requirements.txt    # list of version pinned python dependencies
    ├── .env                    # environment variables
    ├── .gitignore              # .gitignore file
    ├── .pre-commit-config.yml  # pre commit config
    ├── compose.yaml            # docker compose file
    └── README.md               # this readme file
    

## Setup

### Clone repo
```shell script
git clone https://github.com/raphiniert/fastapi-vue.git
cd fastapi-vue
```

#### Local developemmnt

```shell script
docker compose up -d
```
