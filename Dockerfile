# --------------------------
# Stage 1 - Builder
# --------------------------

FROM python:3.11-slim AS builder


WORKDIR /app

# Install build tools

RUN apt-get update && apt-get install -y gcc

COPY requirements.txt .

# Install dependencies into a separate folder 
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ------------------------
# Stage 2 -Runtime
# -----------------------    

FROM python:3.11-slim

WORKDIR /app
# Copy only installed deendencies from builder

COPY --from=builder /install /usr/local

#Copy app code

COPY main.py .

# Expost FastAPI port

EXPOSE 8000

# Run FastAPI
CMD ["uvicorn","main:app", "--host", "0.0.0.0", "--port", "8000"]
