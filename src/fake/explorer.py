from model.explorer import Explorer

_explorers = [
    Explorer(name = "John Doe", country = "United States", description = "John Doe is a software engineer"),
    Explorer(name = "Jane Doe", country = "United States", description = "Jane Doe is a software engineer"),
    Explorer(name = "Jim Doe", country = "United States", description = "Jim Doe is a software engineer"),
]

# get all explorers
def get_all_explorers() -> list[Explorer]:
    """
    Get all explorers
    """
    return _explorers


#get one explorer by name 
def get_explorer_by_name(name: str) -> Explorer | None:
    """
    Get one explorer by name
    """
    return next((explorer for explorer in _explorers if explorer.name == name), None)

#create an explorer
def create_one_explorer(explorer: Explorer) -> Explorer:
    """
    Create an explorer
    """
    _explorers.append(explorer)
    return explorer

#modify an explorer
def modify_one_explorer(name: str, explorer: Explorer) -> Explorer | None:
    """
    Modify an explorer
    """
    for i, e in enumerate(_explorers):
        if e.name == name:
            _explorers[i] = explorer
            return _explorers[i]
    return None

#delete an explorer
def delete_one_explorer(name: str) -> bool:
    """
    Delete an explorer
    """
    for i, e in enumerate(_explorers):
        if e.name == name:
            _explorers.pop(i)
            return True
    return False