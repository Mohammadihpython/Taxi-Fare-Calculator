install:
    #install command
	pip install --upgrade pip &&\
	    pip install -r requirements.txt
format:
    #format code	
lint:
    #flake8 or pylint
test:
    # test
deploy:
    #deploy command

all: install format lint test deploy