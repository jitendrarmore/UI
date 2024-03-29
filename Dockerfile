FROM python:2.7
MAINTAINER JItendra More

# Creating Application Source Code Directory
RUN mkdir -p /opt/src

# Setting Home Directory for containers
WORKDIR /opt/src

# Installing python dependencies
COPY requirements.txt /opt/src
RUN pip install --no-cache-dir -r requirements.txt

# Copying src code to Container
COPY . /opt/src/app

# Application Environment variables
ENV APP_ENV development

# Exposing Ports
EXPOSE 5000

# Setting Persistent data
VOLUME ["/app-data"]

# Running Python Application
CMD ["python", "/opt/src/app/app.py"]
