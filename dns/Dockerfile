FROM ubuntu/bind9:latest

COPY dns-files/named.conf /etc/bind/named.conf
COPY dns-files/l1-9.zone /etc/bind/l1-9.zone

RUN apt-get update
RUN chown -R bind:bind /etc/bind/
RUN chmod 770 /etc/bind/

CMD ["/usr/sbin/named", "-g", "-c", "/etc/bind/named.conf", "-u", "bind"]
