FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "flask" ]

CMD ["--app", "app.py", "--debug", "run" , "--host=0.0.0.0"]