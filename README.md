# Spotify Clone

This a project for the Checkpoint hackaton. It's a music player that resembles Spotify. 

## Stack and Services

- [FastApi](https://fastapi.tiangolo.com/)
- [Vue.js](https://vuejs.org/)
- [React.js](https://reactjs.org/)

## Installation and Usage

### Backend

Use the package manager [pipenv](https://pypi.org/project/pipenv/) to install the dependecies.
Go the backend directory where the Pipfile is and run:

```bash
pipenv install
pipenv shell
```
or

```bash
python -m pipenv install
python -m pipenv shell
```

If you are using WSL then use:

```bash
sudo pipenv install
sudo pipenv shell
```

Once installed you can run the server with the next command:

```bash
uvicorn app.main:app --reload
```

### Frontend-Vue

Work in progress

### Frontend-React

We use [yarn](https://yarnpkg.com/), but you can use npm.
Go to the client-react directory and run the following command:

```bash
yarn
yarn start
```

Now, you have the client with react running.


