FROM python:latest

WORKDIR /app

COPY app .

RUN pip install --upgrade pip >/dev/null && pip install -r requirements.txt >/dev/null

RUN python prepare_lin.py

RUN python prepare_win.py

CMD python cron.py & gunicorn main:app --bind 0.0.0.0:80

# CMD gunicorn main:app --bind 0.0.0.0:80
