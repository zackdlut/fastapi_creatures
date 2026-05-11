from model.creature import Creature

_creatures = [
    Creature(name = "John Doe", country = "United States", area = "Software Engineering", description = "John Doe is a software engineer"),
    Creature(name = "Jane Doe", country = "United States", area = "Software Engineering", description = "Jane Doe is a software engineer"),
    Creature(name = "Jim Doe", country = "United States", area = "Software Engineering", description = "Jim Doe is a software engineer"),
]

def get_all_creatures() -> list[Creature] | None:
    """
    Get all creatures
    """
    return _creatures if _creatures else None

#get one creature by name
def get_creature_by_name(name: str) -> Creature | None:
    """
    Get one creature by name
    """
    return next((creature for creature in _creatures if creature.name == name), None)

#create a creature by creature
def create_one_creature(creature: Creature) -> Creature:
    """
    Create a creature
    """
    _creatures.append(creature)
    return creature

#modify a creature by name
def modify_one_creature(name: str, creature: Creature) -> Creature | None:
    """
    Modify a creature by name
    """
    for i, c in enumerate(_creatures):
        if c.name == name:
            _creatures[i] = creature
            return _creatures[i]
    return None

#delete a creature by name
def delete_one_creature(name: str) -> bool:
    """
    Delete a creature by name   
    """
    for i, c in enumerate(_creatures):
        if c.name == name:
            _creatures.pop(i)
            return True
    return False