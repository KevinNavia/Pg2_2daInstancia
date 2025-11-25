from minivalidator.core import Validator
from minivalidator.rules import NotEmpty, IsEmail, InRange

def test_validator_all_valid():
    rules = {"email": [NotEmpty(), IsEmail()], "age": [InRange(0, 120)]}
    v = Validator(rules)
    data = {"email": "test@example.com", "age": 30}
    assert v.is_valid(data)

def test_validator_some_invalid():
    rules = {"email": [NotEmpty(), IsEmail()], "age": [InRange(0, 120)]}
    v = Validator(rules)
    data = {"email": "bad-email", "age": 200}
    results = v.validate(data)
    assert any(not r.valid for r in results)
