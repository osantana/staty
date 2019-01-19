deps:
	pip install -r requirements-dev.txt

tox: deps
	tox

test:
	py.test

clean:
	-find . -iname "*.py[ocd]" -delete
	-find . -iname "__pycache__" -exec rm -rf {} \;
	-rm -rf dist

release: clean tox
	git push
	git push --tags
	git tag `python setup.py -q version`
	python setup.py sdist upload

update-reqs:
	pip-compile --upgrade requirements-dev.in | uniq > requirements-dev.txt
