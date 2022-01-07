.PHONY: run
run: images11.html images
	python3 main.py

images:
	mkdir images

images11.html:
	wget -4 https://www.hq.nasa.gov/alsj/a11/images11.html
