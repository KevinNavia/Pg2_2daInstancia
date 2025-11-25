import pytest
from minivalidator.rules import NotEmpty, IsEmail, InRange
from minivalidator.errors import ValidationError

@pytest.mark.parametrize("value", [
    "hola",
    "  contenido  ",
    "0",  # non-empty string with whitespace trimmed
])
def test_not_empty_pass(value):
    """Test NotEmpty passes on non-empty strings."""
    NotEmpty().validate(value)

@pytest.mark.parametrize("value", [
    "",
    "   ",
    None,
])
def test_not_empty_fail(value):
    """Test NotEmpty raises ValidationError on empty or None."""
    with pytest.raises(ValidationError):
        NotEmpty().validate(value)

@pytest.mark.parametrize("value", [
    "a@b.com",
    "user.name+tag@domain.co",
])
def test_is_email_pass(value):
    """Test IsEmail passes on valid email strings."""
    IsEmail().validate(value)

@pytest.mark.parametrize("value", [
    "no-email",
    "missing-at.com",
    "@missing-user.com",
    None,
    123,
])
def test_is_email_fail(value):
    """Test IsEmail raises ValidationError on invalid email formats or non-string."""
    with pytest.raises(ValidationError):
        IsEmail().validate(value)

@pytest.mark.parametrize("value", [
    0,
    5,
    10,
    0.0,
    10.0,
    "5",
])
def test_inrange_pass(value):
    """Test InRange passes on numeric values within range [0, 10]."""
    InRange(0, 10).validate(value)

@pytest.mark.parametrize("value", [
    "abc",
    None,
    [],
])
def test_inrange_fail_non_numeric(value):
    """Test InRange raises ValidationError on non-numeric inputs."""
    with pytest.raises(ValidationError):
        InRange(0,10).validate(value)

@pytest.mark.parametrize("value", [
    -1,
    11,
    20,
])
def test_inrange_fail_bounds(value):
    """Test InRange raises ValidationError on values out of bounds [0, 10]."""
    with pytest.raises(ValidationError):
        InRange(0, 10).validate(value)
