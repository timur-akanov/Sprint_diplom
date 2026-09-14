# Sprint_diplom

API autotests for the QA Desk service.

## Requirements
- Python 3.11+
- pip

## Install dependencies

```bash
pip install -r requirements.txt
```

## Environment setup

Create a `.env` file in the project root:

```env
LOGIN=your_login
PASSWORD=your_password
```

You can copy the template:

```bash
cp .env.example .env
```

## Run tests

```bash
pytest -q test
```

## Project structure

- `test/` — API test modules grouped by functionality
- `data/` — common test data
- `helpers/` — utilities: email generation and API wrappers
- `.env.example` — example environment file
- `.gitignore` — ignored local secrets

## Notes

- The tests target the live API at `https://qa-desk.education-services.ru/api`.
- The project uses `requests` and pytest.
- Real credentials are kept in `.env` and are not committed to Git.
- Before running tests, ensure the local `.env` file is created and contains valid values.
