pythonprefix := $(shell ~/.pyenv/bin/pyenv prefix)

run:
	cd src;PYTHONPATH= python3 mail_app.py
deps:
	pip3 install -r requirements.txt --prefix=${pythonprefix}
