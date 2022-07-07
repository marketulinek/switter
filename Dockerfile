# This dockerfile is only meant for local development
FROM python:3.9-slim

# Running as non-root user
ENV APP_USER=appuser
RUN useradd -m $APP_USER

# prevent Python from copying pyc files to the container
ENV PYTHONDONTWRITEBYTECODE 1
# ensures that Python output is logged to the terminal, making it possible to monitor Django logs in realtime
ENV PYTHONUNBUFFERED 1

# install and upgrade the pip version that is in the container
RUN pip install --upgrade pip

# copy the requirements.txt file into the work directory in the container
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy all the project source code to the working directory in the container
COPY . .

USER $APP_USER

# set the executable commands in the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]