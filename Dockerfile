# Specifying base image
FROM python:3.11.5

# Setting a work directory
WORKDIR /app

# Copying requirements.txt to the working directory
COPY requirements.txt ./ 

# Installing requirements
RUN pip install -r requirements.txt 

# Copying the rest of the code to the working directory
COPY . . 

# Command to run on container start
CMD ["python", "src/main.py"]