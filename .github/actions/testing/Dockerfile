FROM python:3.10
LABEL authors="shamsoddin"
COPY first.py /first.py
COPY /common/*.py /common
RUN la -a
ENTRYPOINT ["python", "/first.py"]
