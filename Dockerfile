FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /project

COPY requirements.txt .

RUN apt update && apt upgrade -y && apt autoremove -y \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]