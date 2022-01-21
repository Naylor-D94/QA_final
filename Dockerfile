FROM python:3

WORKDIR /usr/webapp

RUN pip install flask
RUN pip install flask-mysqldb
RUN pip install pytest 

COPY ./webapp/app.py app.py

EXPOSE 5000

CMD [ "python", "app.py" ]


