FROM centos:7

USER root

RUN useradd service-user && \
    yum install -y epel-release && \
    yum install -y nginx gettext

COPY application /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf.template
COPY entrypoint.sh /opt/entrypoint.sh

CMD [ "/opt/entrypoint.sh" ]
