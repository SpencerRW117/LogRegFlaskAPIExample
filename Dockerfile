# Use the official Python image as a base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python application files to the container
COPY redacted_model_app.py .
COPY model.pkl .

# Expose port 1313
EXPOSE 8080

# Define the command to run your application
CMD ["python3", "LR_Model_App.py"]
