FROM python:3.9-slim-buster as build

# set the working directory in the container
WORKDIR /app

# copy the requirements file
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the application's source code into the container
COPY . .

# expose the port that the service listens on
EXPOSE 80

# run
CMD ["python3", "-u", "bitcoin_service.py"]

