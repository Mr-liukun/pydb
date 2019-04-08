
FROM python:3.6.7

RUN mkdir -p /usr/src/pydb

COPY .  /usr/src/pydb/

WORKDIR /usr/src/pydb/

#防止requests超时，含数据库需要
RUN pip --default-timeout=100 install -U requests
#防止requests超时
#放最后
ADD requirements.txt /usr/src/pydb/
RUN pip install -r requirements.txt


CMD [ "sh", "./run_web.sh"]
