# Usar la imagen de node
FROM node:16

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos package.json y package-lock.json al contenedor
COPY package*.json ./

# Instalar las dependencias
RUN npm install

# Copiar todo el contenido del proyecto al contenedor
COPY . .

# Construir la aplicación React
RUN npm run build

# Exponer el puerto 3000
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["npm", "start"]
