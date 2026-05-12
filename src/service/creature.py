from model.creature import Creature
import fake.creature as data

def get_all_creatures() -> list[Creature] | None:
    return data.get_all_creatures()

def get_creature_by_name(name: str) -> Creature | None:
    return data.get_creature_by_name(name)

def create_one_creature(creature: Creature) -> Creature:
    return data.create_one_creature(creature)

def modify_one_creature(name: str, creature: Creature) -> Creature | None:
    return data.modify_one_creature(name, creature)
def delete_one_creature(name: str) -> bool:
    return data.delete_one_creature(name)