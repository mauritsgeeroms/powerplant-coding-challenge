
FROM python:3.9
WORKDIR /app
COPY ./python-app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./python-app /app
CMD ["fastapi", "run", "main.py", "--port", "8888"]