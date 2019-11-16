install:
	pip install -r requirements.txt

cook-data:
	python src/cook_data.py

init-db:
	python src/init_db.py

map-counters:
	python src/map_counters.py

map-weekdays:
	python src/map_weekdays.py

convert-counters:
	python src/convert_counters.py
