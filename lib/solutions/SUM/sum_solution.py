# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y: int) -> int:
    # raise NotImplementedError()
    
    if x > 100 or x < 0:
        raise ValueError(f"x={x} is not between 0 - 100")
    elif y > 100:
        raise ValueError(f"y={y} is not between 0 - 100")
    
    return x + y

