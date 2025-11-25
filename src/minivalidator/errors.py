"""Excepciones y tipos para minivalidator."""
from typing import Any

class ValidationError(Exception):
    """Excepción lanzada cuando una validación falla."""
    def __init__(self, message: str, value: Any = None):
        super().__init__(message)
        self.value = value
