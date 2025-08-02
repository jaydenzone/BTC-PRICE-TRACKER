FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Copy app code
COPY . .

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 10000

# Start the app
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
