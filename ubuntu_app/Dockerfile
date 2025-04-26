# hadolint ignore=ALL
# trunk-ignore(hadolint)

FROM ubuntu:20.04 

RUN apt-get update 

RUN apt-get install -y python3 python3-pip curl

# trunk-ignore(hadolint/DL3013)
RUN pip3 install flask-restx 

ADD ubuntu_app.py /usr 

EXPOSE 5000 
# trunk-ignore(hadolint/DL3013)
CMD python3 /usr/ubuntu_app.py 