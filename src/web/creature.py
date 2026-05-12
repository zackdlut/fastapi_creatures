from fastapi import APIRouter
from model.creature import Creature
import service.creature as service

router = APIRouter(prefix = "/creature", tags = ["creature"])

@router.get("/")
def get_all_creatures() -> list[Creature]:
    return service.get_all_creatures()

@router.get("/{name}")
def get_one_creature(name: str) -> Creature | None:
    return service.get_creature_by_name(name)

@router.post("/")
def create_one_creature(creature: Creature) -> Creature:
    return service.create_one_creature(creature)

@router.put("/{name}")
def modify_one_creature(name: str, creature: Creature) -> Creature | None:
    return service.modify_one_creature(name, creature)

@router.delete("/{name}")
def delete_one_creature(name: str) -> bool:
    return service.delete_one_creature(name)