.PHONY: package
package:
	@./setup.py sdist

.PHONY: clean
clean:
	rm -rf MANIFEST
	rm -rf dist

.PHONY: publish
publish: clean package
	twine upload dist/*
