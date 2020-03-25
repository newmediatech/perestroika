FROM python:3.8

COPY dev-requirements.txt /var/perestroika/dev-requirements.txt
COPY requirements.txt /var/perestroika/requirements.txt
RUN pip install -r /var/perestroika/dev-requirements.txt
RUN pip install -r /var/perestroika/requirements.txt
WORKDIR /var/perestroika
ENV PYTHONPATH "${PYTHONPATH}:/var/perestroika/perestroika"
ENV PYTHONPATH "${PYTHONPATH}:/var/perestroika/tests"
