FROM ubuntu
RUN apt-get update
RUN apt-get install -y python2.7
RUN apt-get install -y pip
RUN pip install flask
RUN pip install tk
RUN pip install flask-mysql
COPY . /opt/ravi-app
#RUN git clone XYZ
#https://stackoverflow.com/questions/20632258/change-directory-command-in-docker
WORKDIR "/opt/ravi-app"
RUN pip install -r requirement.txt
# . means current folder 
#Any RUN, CMD, ADD, COPY, or ENTRYPOINT command will be executed in the specified working directory.


ENTRYPOINT FLASK_APP=/opt/ravi-app/basic_app.py flask run