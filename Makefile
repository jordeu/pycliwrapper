SHELL := /bin/bash
.PHONY: all fusionfs

publish:
	rm -rf dist/
	python3 setup.py sdist
	twine upload -r pypi dist/pycliwrapper-*.tar.gz