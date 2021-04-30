import api_requests


class User:
    def __init__(self, user_id: int):
        if not isinstance(user_id, str):
            raise TypeError(f'must be str, not {type(user_id).__name__}')
        self.id = user_id


def is_live(user_id: str):
    if not isinstance(user_id, str):
        raise TypeError(f'must be str, not {type(user_id).__name__}')
    response = api_requests.movies_api(user_id, live_only=True)
    if len(response) == 0:
        return False
    else:
        return True
