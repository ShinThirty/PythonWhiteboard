venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
test: venv/bin/activate
	./venv/bin/black .
	./venv/bin/isort .
	PYTHONPATH=. ./venv/bin/pytest
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf venv
