.PHONY: help venv install run test lint clean

help:
	@echo "Comandos disponibles:"
	@echo "  make venv       Crea un entorno virtual."
	@echo "  make install    Instala las dependencias del proyecto."
	@echo "  make run        Ejecuta la aplicación."
	@echo "  make test       Ejecuta las pruebas."
	@echo "  make lint       Ejecuta el linter (flake8)."
	@echo "  make clean      Elimina el entorno virtual y archivos de compilación."

venv:
	python -m venv venv

install: venv
	venv\Scripts\activate && pip install -r requirements.txt

run:
	venv\Scripts\activate && uvicorn app.api.main:app --reload

test:
	venv\Scripts\activate && pytest

lint:
	venv\Scripts\activate && flake8 --config=.flake8

clean:
	rm -rf venv
