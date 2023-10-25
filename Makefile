help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

tests: ## Run the tests using pytest
	pytest

coverage: ## Generate a report of the test coverage
	coverage run -m pytest && coverage report

startmodule: ## Start a new module. use make startmodule MODULE_NAME=starship
	mkdir -p src/modules/$(MODULE_NAME)/domain
	mkdir -p src/modules/$(MODULE_NAME)/infrastructure
	mkdir -p src/modules/$(MODULE_NAME)/application
	touch src/modules/$(MODULE_NAME)/__init__.py
	touch src/modules/$(MODULE_NAME)/domain/__init__.py
	touch src/modules/$(MODULE_NAME)/domain/$(MODULE_NAME).py
	touch src/modules/$(MODULE_NAME)/domain/$(MODULE_NAME)_id.py
	touch src/modules/$(MODULE_NAME)/domain/$(MODULE_NAME)_repository.py
	touch src/modules/$(MODULE_NAME)/infrastructure/__init__.py
	touch src/modules/$(MODULE_NAME)/application/__init__.py

shell: ## Interactive shell
	python3 shell.py
