all: build run

build:
	docker build . --tag pydata_example

run:
	mkdir -p data
	docker run -v $(shell pwd)/data:/app/data pydata_example

clobber:
	rm -fR data
