FROM node:14

COPY ./package.json /app/
WORKDIR /app
RUN yarn global add @vue/cli @vue/cli-service
RUN yarn install

COPY . /app

ENTRYPOINT yarn serve