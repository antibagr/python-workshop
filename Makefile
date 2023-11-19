﻿SOURCES = WorkShop

.DEFAULT_GOAL := help

help: ## Display this help screen
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.PHONY: help

install: ## Install project dependencies
	poetry install --no-interaction --no-ansi --no-root
.PHONY: install

format: ## Format the source code
	poetry run black $(SOURCES)
	poetry run isort $(SOURCES)
.PHONY: format

lint: ## Lint the source code
	poetry run black --check $(SOURCES)
	poetry run isort --check $(SOURCES)

	poetry run flake8 $(SOURCES)
	poetry run mypy $(SOURCES)
	poetry run bandit -c pyproject.toml -r ${SOURCES}
	ggshield secret scan repo .

.PHONY: lint