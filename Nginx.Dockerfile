FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

COPY static /usr/share/nginx/html/static
COPY media /usr/share/nginx/html/media

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]