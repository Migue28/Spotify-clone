# Spotify Clone

This a project for the Checkpoint hackaton. It's a music player that resembles Spotify. 

## Stack and Services

- [Vue.js](https://vuejs.org/)
- [FastApi](https://fastapi.tiangolo.com/)

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

### Frontend

Work in progress
