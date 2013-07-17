default: all

all: test

dependencies:
	@pip install -r test-requirements.txt

clean:
	@find . -name "*.pyc" -delete

test: dependencies clean
	@echo "Running all tests..."
	nosetests
