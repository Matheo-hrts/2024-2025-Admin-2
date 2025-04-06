FROM nginx:1.27.4

COPY web-files/config/nginx.conf /etc/nginx/nginx.conf
COPY web-files/certificate/nginx-selfsigned.crt /etc/ssl/certs/nginx-selfsigned.crt
COPY web-files/certificate/nginx-selfsigned.key /etc/ssl/private/nginx-selfsigned.key

RUN apt-get update
RUN apt install certbot python3-certbot-nginx -y

