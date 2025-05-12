# Base Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "src/api/app.py"]