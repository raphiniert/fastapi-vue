FROM python:3.10-alpine

ARG PROJECT_NAME demo
WORKDIR /srv/$PROJECT_NAME

# Ensure we have the latest pip version
RUN pip install pip --upgrade
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./api /srv/$PROJECT_NAME/api

ENV PYTHONPATH=/srv/$PROJECT_NAME

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
