FROM debian

RUN apt update -y
RUN apt install python3 -y
RUN apt install apache2 -y
RUN apt install php -y
RUN apt install systemctl

COPY source/index.html /var/www/html/
COPY source/getSched.php /var/www/html/
COPY source/root-cont /

RUN chmod 777 /input.txt
RUN chmod 777 /startup.sh

EXPOSE 80
CMD /startup.sh
