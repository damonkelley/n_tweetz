FROM python:3.4
ENV PYTHONUNBUFFERED 1
ENV TERM xterm-256color
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

CMD python n_tweetz.py $N $USERNAME
