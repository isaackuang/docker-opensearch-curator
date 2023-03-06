FROM isaackuang/alpine-base:3.16

RUN apk --no-cache --progress add python3 py3-pip

RUN pip3 install curator-opensearch --ignore-installed six

