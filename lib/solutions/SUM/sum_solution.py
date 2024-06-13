# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y: int) -> int:
    # raise NotImplementedError()
    
    if not isinstance(x, int):
        raise ValueError(f"x={x} is not of type int")
    if not isinstance(y, int):
        raise ValueError(f"y={x} is not of type int")
    
    if x > 100 or x < 0:
        raise ValueError(f"x={x} is not an integer between 0 - 100")
    if y > 100 or y < 0:
        raise ValueError(f"y={y} is not an integer between 0 - 100")
    
    return x + y


