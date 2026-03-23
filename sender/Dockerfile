FROM nginx:alpine

# Remplacement de la config Nginx par defaut
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Ajout du fichier web statique
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
