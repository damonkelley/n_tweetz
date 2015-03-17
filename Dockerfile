FROM python:3.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "n_tweetz.py"]
CMD ["--help"]
