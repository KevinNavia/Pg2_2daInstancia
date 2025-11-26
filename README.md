# Minivalidator

Pequeña librería de validadores reutilizables para Python.

## Descripción

Minivalidator es una librería ligera que proporciona reglas de validación reutilizables para validar datos en aplicaciones Python. Incluye validadores comunes como verificación de cadenas no vacías, formato de email y rangos numéricos.

## ESTRUCTURA 
minivalidator/               # repo root
├─ src/
│  └─ minivalidator/
│     ├─ __init__.py
│     ├─ core.py            # módulo principal (core)
│     ├─ rules.py           # submódulo 1: reglas/validadores
│     └─ errors.py          # submódulo 2: excepciones y tipos
├─ tests/
│  ├─ test_core.py
│  └─ test_rules.py
├─ pyproject.toml
├─ setup.cfg
├─ README.md
├─ LICENSE
└─ requirements_dev.txt


## Instalación

Puedes instalar Minivalidator usando pip:

```bash
pip install minivalidator
```

O desde el código fuente:

```bash
git clone <https://github.com/KevinNavia/Pg2_2daInstancia.git>
cd minivalidator
pip install .
```

## Uso

### Importar la librería

```python
from minivalidator.rules import NotEmpty, IsEmail, InRange
from minivalidator.errors import ValidationError
```

### Ejemplos de uso

#### NotEmpty
Valida que una cadena no esté vacía.

```python
validator = NotEmpty()
try:
    validator.validate("hola")  # Pasa
    validator.validate("")      # Lanza ValidationError
except ValidationError as e:
    print(e)
```

#### IsEmail
Valida el formato de un email.

```python
validator = IsEmail()
try:
    validator.validate("user@example.com")  # Pasa
    validator.validate("invalid-email")     # Lanza ValidationError
except ValidationError as e:
    print(e)
```

#### InRange
Valida que un número esté dentro de un rango.

```python
validator = InRange(0, 10)
try:
    validator.validate(5)    # Pasa
    validator.validate(15)   # Lanza ValidationError
except ValidationError as e:
    print(e)
```

## API

### Clases de Validación

- `Rule`: Clase base abstracta para reglas de validación.
- `NotEmpty`: Valida que el valor no sea None o una cadena vacía.
- `IsEmail`: Valida que el valor sea una cadena con formato de email válido.
- `InRange(min_, max_)`: Valida que el valor numérico esté dentro del rango especificado.

### Excepciones

- `ValidationError`: Excepción lanzada cuando una validación falla. Incluye el mensaje de error y el valor inválido.

## Pruebas

Para ejecutar las pruebas, instala pytest y ejecuta:

```bash
pytest
```

O específicamente para las pruebas de reglas:

```bash
pytest test/test_rules.py

```
## para probar pypi 
'''
twine upload --repository testpypi --username LAPSUPdead --password LAPSUPdead1012 --verbose dist/*
'''
## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

## Autor

Kevin Navia Matienzo - kevinnavia68@gmail.com

## link pypi
https://pypi.org/project/minivalidator/0.1.0/
