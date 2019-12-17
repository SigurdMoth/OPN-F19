FROM python:3.7-alpine

RUN pip3 install Flask
RUN pip install mysql-connector-python

COPY . .

CMD python3 ./server.py


#port server.py localhost:5000
#port server.py mysql connection= 3306
#port mysql 33060 (3306)
#expose ports in composefile for flaskserver