ARG BASE_CONTAINER=jupyter/scipy-notebook
FROM $BASE_CONTAINER

USER root

RUN apt-get update

RUN pip install --upgrade pip setuptools wheel

ADD requirements.txt /project/

RUN cd /project && pip install --pre -r requirements.txt

ADD . /project

WORKDIR /

CMD ["jupyter", "lab", "--allow-root"]

