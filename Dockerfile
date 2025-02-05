# .Dockerfile

# Use a minimal Python 3.9 image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies with caching
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

# Copy all application files at once
COPY . .

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' botuser && chown -R botuser:botuser /app
USER botuser

# Run the bot
CMD ["python", "main.py"]
