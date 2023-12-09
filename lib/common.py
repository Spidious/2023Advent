def getFile(f: str) -> list:
    with open(f, 'r') as file:
        inlist = [fp[:-1] for fp in file]
    return inlist