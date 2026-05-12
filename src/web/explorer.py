from fastapi import APIRouter
from model.explorer import Explorer
import service.explorer as service

router = APIRouter(prefix = "/explorer", tags = ["explorer"])

@router.get("/")
def get_all_explorers() -> list[Explorer]:
    return service.get_all_explorers()

@router.get("/{name}")
def get_one_explorer(name: str) -> Explorer | None:
    return service.get_explorer_by_name(name)

@router.post("/")
def create_one_explorer(explorer: Explorer) -> Explorer:
    return service.create_one_explorer(explorer)

@router.put("/{name}")
def modify_one_explorer(name: str, explorer: Explorer) -> Explorer | None:
    return service.modify_one_explorer(name, explorer)

@router.delete("/{name}")
def delete_one_explorer(name: str) -> bool:
    return service.delete_one_explorer(name)