"""Core de la librería: Validator que aplica reglas a campos."""
from typing import Dict, List, Any
from .errors import ValidationError
from .rules import Rule

class FieldValidationResult:
    def __init__(self, field: str, valid: bool, errors: List[ValidationError]):
        self.field = field
        self.valid = valid
        self.errors = errors

class Validator:
    """
    Validator aplica reglas a un dict de datos.
    rules_map example: {"email": [IsEmail(), NotEmpty()], "age": [InRange(0,120)]}
    """
    def __init__(self, rules_map: Dict[str, List[Rule]]):
        self.rules_map = rules_map

    def validate(self, data: Dict[str, Any]) -> List[FieldValidationResult]:
        results = []
        for field, rules in self.rules_map.items():
            errors = []
            value = data.get(field)
            for rule in rules:
                try:
                    rule.validate(value)
                except ValidationError as e:
                    errors.append(e)
            results.append(FieldValidationResult(field, len(errors) == 0, errors))
        return results

    def is_valid(self, data: Dict[str, Any]) -> bool:
        return all(r.valid for r in self.validate(data))
