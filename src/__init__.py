from src.cache import Cache
from src.dropbox_client import DropboxClient
from src.local_file_client import LocalFileClient
import dropbox

# TOKEN = "sl.Bb9h5aVG8RbW5e0RyKB6y1q0s-qo27ZNDv6RAbAiwG9V1fQnlPcCiHRi0P__XEljwwFar9t1VFYddG5CNNWyBt7cMTTMUr4IaGbabyYZEw5IlPBJTGNBIPnJes0qjQuQbviqKAI"

# c = Cache(DropboxClient())

c = Cache(LocalFileClient())


@c.cache_factory("./cache/ticker_{}.json", 60 * 60 * 24)
def test(ticker: str, other: str):
    print("Calling method directly")
    return {"test_method": True, "ticker": ticker}


@c.cache_factory("./cache/ticker.json", 60)
def test_no_params(ticker: str, other: str):
    print("Calling method directly")
    return {"test_method": True, "ticker4": ticker}


if __name__ == "__main__":
    from pprint import pprint

    res = test_no_params("AAPL", "altceva")
    pprint(res)
    auth = dropbox.DropboxOAuth2FlowNoRedirect(
        "l6o3uw97luokkx5", "4v1rpadngy3o5vg", token_access_type="offline"
    )
    pprint(auth.start())
    pprint(auth.code_challenge)
    pprint(auth.code_verifier)
    # CODE = "z0yGqNuoZwAAAAAAAAABWCdIzDIu00CeMY8YlW9dt6Q"

    # # pprint(auth.start())
    # res = auth.finish(CODE)
    # pprint(res.access_token)
    # pprint(res.refresh_token)
    # pprint(res.expires_at)
