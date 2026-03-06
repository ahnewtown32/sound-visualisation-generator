FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements-dev.txt /app/
RUN python -m pip install --upgrade pip \
 && pip install -r requirements.txt -r requirements-dev.txt

COPY . /app
RUN pip install -e .

CMD ["bash"]