FROM python:3
WORKDIR /action
ADD ./entrypoint.py .
RUN pip install docopt
ENTRYPOINT ["python", "/action/entrypoint.py"]
