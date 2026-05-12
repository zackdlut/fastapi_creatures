from model.creature import Creature
from service import creature as code

sample = Creature(
    name = "John Doe",
    country = "United States",
    area = "Software Engineering",
    description = "John Doe is a software engineer",
    aka = "John",
)

def test_create_one_creature():
    result = code.create_one_creature(sample)
    assert result is not None
    assert result.name == sample.name
    assert result.country == sample.country
    assert result.area == sample.area
    assert result.description == sample.description
    assert result.aka == sample.aka

def test_get_one_creature():
    result = code.get_creature_by_name(sample.name)
    assert result is not None
    assert result.name == sample.name
    assert result.country == sample.country
    assert result.area == sample.area
    assert result.description == sample.description
    assert result.aka == sample.aka

def test_get_missing_creature():
    result = code.get_creature_by_name("Missing")
    assert result is None

def test_modify_one_creature():
    result = code.modify_one_creature(sample.name, sample)
    assert result is not None
    assert result.name == sample.name
    assert result.country == sample.country
    assert result.area == sample.area
    assert result.description == sample.description
    assert result.aka == sample.aka