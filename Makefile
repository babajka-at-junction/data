install:
	pip install -r requirements.txt

init-db:
	python init-db.py

map-counters:
	python map-counters.py

convert-counters:
	python convert-counters.py
