from model.explorer import Explorer
import fake.explorer as data

def get_all_explorers() -> list[Explorer] | None:
    return data.get_all_explorers()

def get_explorer_by_name(name: str) -> Explorer | None:
    return data.get_explorer_by_name(name)

def create_one_explorer(explorer: Explorer) -> Explorer:
    return data.create_one_explorer(explorer)

def modify_one_explorer(name: str, explorer: Explorer) -> Explorer | None:
    return data.modify_one_explorer(name, explorer)

def delete_one_explorer(name: str) -> bool:
    return data.delete_one_explorer(name)