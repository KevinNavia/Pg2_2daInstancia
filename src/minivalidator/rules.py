"""Reglas/validadores reutilizables."""
import re
from typing import Any
from .errors import ValidationError

EMAIL_RE = re.compile(r"^[^@]+@[^@]+\.[^@]+$")

class Rule:
    """Interfaz base para reglas de validación."""
    def validate(self, value: Any) -> None:
        raise NotImplementedError

class NotEmpty(Rule):
    """Valida que una cadena no esté vacía."""
    def validate(self, value: Any) -> None:
        if value is None or (isinstance(value, str) and value.strip() == ""):
            raise ValidationError("Valor vacío", value)

class IsEmail(Rule):
    """Valida formato de email sencillo."""
    def validate(self, value: Any) -> None:
        if not isinstance(value, str) or not EMAIL_RE.match(value):
            raise ValidationError("Email inválido", value)

class InRange(Rule):
    """Valida que un número esté dentro de un rango [min_, max_]."""
    def __init__(self, min_: float = None, max_: float = None):
        self.min_ = min_
        self.max_ = max_

    def validate(self, value: Any) -> None:
        try:
            num = float(value)
        except Exception:
            raise ValidationError("Valor no numérico", value)
        if self.min_ is not None and num < self.min_:
            raise ValidationError(f"Valor {num} < mínimo {self.min_}", value)
        if self.max_ is not None and num > self.max_:
            raise ValidationError(f"Valor {num} > máximo {self.max_}", value)
