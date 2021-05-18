FROM ubuntu:20.04
RUN apt update && apt install -y python3 python3-distutils python3-dev curl git
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py
WORKDIR /app
COPY requirements-web.txt requirements.txt
RUN python3 -m pip install -r requirements.txt
COPY . .
CMD python3 -u web_app.py