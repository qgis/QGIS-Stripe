FROM python:3.6
MAINTAINER Richard Duivenvoorde<richard@duif.net>

RUN  export DEBIAN_FRONTEND=noninteractive
ENV  DEBIAN_FRONTEND noninteractive
RUN  dpkg-divert --local --rename --add /sbin/initctl
#RUN  ln -s /bin/true /sbin/initctl

RUN apt-get -y update

ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt

ADD striped /striped
ADD logs /logs

EXPOSE 8000

#ENTRYPOINT ["gunicorn", "striped:app", "-b", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-"]
ENTRYPOINT ["gunicorn", "striped:app", "-b", "0.0.0.0:8000", "--access-logfile", "/logs/striped-access.log", "--error-logfile", "/logs/striped-error.log"]
