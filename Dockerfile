FROM apify/actor-python:3.11

COPY . ./

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
