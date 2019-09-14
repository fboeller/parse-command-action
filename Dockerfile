FROM python:3
ADD entrypoint.py /
WORKDIR /
RUN pip install docopt
CMD ["python", "entrypoint.py"]
