FROM python:3.10
LABEL authors="shamsoddin"
COPY first.py /first.py
RUN mkdir /common
COPY common/ /common/
RUN la -a
ENTRYPOINT ["python", "/first.py"]
