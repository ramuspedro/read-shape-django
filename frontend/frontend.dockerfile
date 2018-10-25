FROM node:8

LABEL authors="Pedro Ramos"

# Create a directory where our app will be placed
RUN mkdir -p /home/frontend

COPY . /home/frontend

# Change directory so that our commands run inside this new directory
WORKDIR /home/frontend

RUN npm install -g @vue/cli