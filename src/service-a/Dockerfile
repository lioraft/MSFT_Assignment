FROM python:3.9-slim-buster as build

# create a non-root user
RUN useradd -m newuser

# set the working directory in the container
WORKDIR /app

# copy files and adjust ownership
COPY . /app
RUN chown -R newuser:newuser /app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose the port that the service listens on
EXPOSE 80

# Switch to the non-root user
USER newuser

# run
CMD ["python3", "-u", "bitcoin_service.py"]

