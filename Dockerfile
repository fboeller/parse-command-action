FROM python:3
ADD entrypoint.py /
RUN pip install docopt
CMD ["python", "./entrypoint.py"]
