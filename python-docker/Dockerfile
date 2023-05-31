# Pull base image
FROM python:3.11.1
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /NewToDo
# Install dependencies
COPY ../Pipfile Pipfile.lock /NewToDo/
#COPY C:/Users/user/PycharmProjects/calculator/NewToDo/Pipfile Pipfile.lock
RUN pip install pipenv && pipenv install --system
# Copy project
COPY . /NewToDo/