run: 
	python -m whiteboard_service

clean:
	find . -name '*.pyc' -exec rm '{}' ';'
	find . -name '__pycache__' -type d -prune -exec rm -rf '{}' '+'
	find . -name '.pytest_cache' -type d -prune -exec rm -rf '{}' '+'

scrub: clean
	find . -name '*.egg-info' -type d -prune -exec rm -rf '{}' '+'
	rm -rf htmlcov
	rm -f .coverage

format:
	isort -rc whiteboard_service tests
	black whiteboard_service tests

test:
	python3 -m coverage run --source whiteboard_service -m pytest tests -p no:warnings
	coverage report -m

review: format test

generate:
	python -m grpc.tools.protoc --proto_path=./whiteboard_service/stubs --python_out=./whiteboard_service/stubs --grpc_python_out=./whiteboard_service/stubs whiteboard.proto 
