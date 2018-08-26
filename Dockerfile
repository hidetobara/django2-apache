FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y apt-utils vim less curl apache2 apache2-utils mysql-client python3 libapache2-mod-wsgi-py3
RUN ln /usr/bin/python3 /usr/bin/python
RUN apt-get -y install python3-pip
RUN ln /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip
RUN pip install django ptvsd PyMySQL
ADD ./web.conf /etc/apache2/sites-available/000-default.conf
EXPOSE 80 8080
CMD ["apache2ctl", "-D", "FOREGROUND"]
