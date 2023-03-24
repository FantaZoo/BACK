FROM --platform=$BUILDPLATFORM python AS back
COPY requirements.txt .
RUN apt-get update && apt-get install -y libsnappy-dev && apt-get clean
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

WORKDIR /back
CMD ["sh", "-c", "python manage.py makemigrations fantazoo && python manage.py migrate && python manage.py runserver"]

FROM nginx:alpine AS app

COPY --from=back . /usr/share/nginx/html