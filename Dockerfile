FROM --platform=$BUILDPLATFORM python AS back
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y libsnappy-dev && apt-get clean
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/back
CMD ["sh", "-c", "python manage.py makemigrations fantazoo && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]