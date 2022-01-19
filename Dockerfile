FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
RUN python manage.py test