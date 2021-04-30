import requests


def movies_api(user_id: str, live_only: bool):
    if live_only:
        r = requests.get(f"https://public.openrec.tv/external/api/v5/movies?channel_id={user_id}&onair_status=1")
    else:
        r = requests.get(f"https://public.openrec.tv/external/api/v5/movies?channel_id={user_id}")
    return r.json()


def captures_api(captured_by_id: str = None, channel_id: str = None):
    args = {}
    if captured_by_id:
        args["captured_user_id"] = captured_by_id
    if channel_id:
        args["channel_id"] = channel_id
    r = requests.get(f"https://public.openrec.tv/external/api/v5/captures", params=args)
    return r.json()
