FROM node:14

COPY ./package.json /app/
WORKDIR /app
RUN npm install --global @vue/cli @vue/cli-service
RUN npm install

COPY . /app

ENTRYPOINT npm run serve