#Proxy
FROM nginx:latest
RUN rm /etc/nginx/conf.d/default.conf
#bash ind i container docker exec -it opn-f19_proxy_1 for at se at filer ligger der
COPY domain.crt /etc/nginx/
COPY domain.key /etc/nginx/
COPY html /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
#COPY nginx.conf /etc/nginx
#COPY insert.html /usr/share/nginx/html