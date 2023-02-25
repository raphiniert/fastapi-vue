FROM python:3.10-alpine as base

ARG PROJECT_NAME demo
WORKDIR /srv/$PROJECT_NAME

# Ensure we have the latest pip version
RUN pip install pip --upgrade
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./api /srv/$PROJECT_NAME/api

ENV PYTHONPATH=/srv/$PROJECT_NAME

FROM base as prod
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

FROM base as dev
# install dev dependencies and copy tests
COPY requirements-dev.txt requirements-dev.txt
RUN pip install -r requirements-dev.txt
COPY ./tests /srv/$PROJECT_NAME/tests

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
