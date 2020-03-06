FROM centos:7

USER root

RUN useradd service-user && \
    yum install -y epel-release && \
    yum install -y python3 python3-pip

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt && \
    rm -f /tmp/requirements.txt

COPY application /opt/application

RUN chown -R service-user:service-user /opt/application

WORKDIR /opt/application

USER service-user

CMD [ "python3", "/opt/application/main.py" ]

