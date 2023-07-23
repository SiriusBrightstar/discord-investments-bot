FROM python:slim

RUN mkdir investments_bot
COPY investments_bot/. /investments_bot
RUN pip3 install -r /requirments.txt

WORKDIR /investments_bot

CMD ["python3", "main.py"]