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

release:
	git push origin master
	git tag `python setup.py -q version`
	git push origin master --tags
	rm -rf dist/*
	python setup.py sdist
	twine check dist/*
	twine upload dist/*

update-reqs:
	pip-compile --upgrade requirements-dev.in | uniq > requirements-dev.txt
