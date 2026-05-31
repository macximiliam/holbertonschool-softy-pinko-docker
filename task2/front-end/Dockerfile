# 1. Utilizar la versión más reciente de Nginx como base
FROM nginx:latest

# 2. Copiar los archivos estáticos del repositorio al directorio web de Nginx
COPY ./softy-pinko-front-end /var/www/html/softy-pinko-front-end

# 3. Copiar la configuración personalizada para reemplazar la configuración por defecto
COPY ./softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf

