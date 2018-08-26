* This is Django Dokcker project using MySQL, Apache2.

* build and start
$ docker-compose up -d

$ docker exec -it [ID] bash

$$ python3 manage.py migrate
$$ python3 manage.py runserver 0.0.0.0:8080

* browing
http://localhost:80/ -> using Apache
http://localhost:8080/ -> using runserver for develop

* stop
$ docker-compose down


And
enjoy it.
