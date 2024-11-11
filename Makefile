build_and_run:
	docker build -t api .
	
	docker run -d --name engie_api -p 8888:8888 api