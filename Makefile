install:
	poetry install

test:
	poetry run pytest -s

test-coverage:
	poetry run pytest --cov=lessons --cov-report xml

lint:
	poetry run flake8 lessons

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
