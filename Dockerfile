FROM python:3.7

EXPOSE 8000

COPY . .

WORKDIR /GamerAlley
    RUN pip3 install -r requirements.txt
    RUN python3 manage.py makemigrations
    RUN python3 manage.py migrate

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

