FROM python:3.9-slim-buster as build

# create a non-root user
RUN useradd -m newuser

# set the working directory
WORKDIR /app

# copy files and adjust ownership
COPY . /app
RUN chown -R newuser:newuser /app

# Switch to the non-root user
USER newuser

# run
CMD ["python3", "app.py"]
