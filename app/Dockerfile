FROM python:3.7-alpine

LABEL maintainer="Ivan Masnari ivanmasnari94@gmail.com"

ENV GROUP_ID=1000 \
    USER_ID=1000 

WORKDIR /var/www

ADD ./requirements.txt /var/www/requirements.txt
RUN pip install -r requirements.txt
ADD . /var/www
RUN pip install gunicorn

RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh
RUN chown -R www:www /var/www
USER www

EXPOSE 5000

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]

