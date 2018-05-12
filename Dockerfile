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

#ADD server.py /server.py
# Open port 8080 so linked containers can see them
#EXPOSE 8080
#CMD ["python", "/server.py"]

EXPOSE 8000
ENTRYPOINT ["gunicorn", "striped:app", "-b", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-"]
#CMD ["striped:app"]