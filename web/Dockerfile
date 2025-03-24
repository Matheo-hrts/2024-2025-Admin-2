FROM nginx:latest

COPY web-files/config/nginx.conf /etc/nginx/nginx.conf
COPY web-files/html/www/index.html /var/www/html/www/index.html
COPY web-files/html/www/products.php /var/www/html/www/products.php
COPY web-files/html/blog/blog.html /var/www/html/blog/blog.html

RUN apt-get update
