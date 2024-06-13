

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str) -> str:
    # raise NotImplementedError()
    
    if not isinstance(friend_name, str):
        raise ValueError(f"{friend_name} is not of type string")
    
    return friend_name

