FROM python:3.8

COPY . .

RUN pip install -r requirements.txt

WORKDIR .

CMD python app.py
