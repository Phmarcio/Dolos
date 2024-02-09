FROM python=3.10-slim

WORKDIR /app
COPY . /app

RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py", "--debug", "run", "--host=0.0.0.0" ]