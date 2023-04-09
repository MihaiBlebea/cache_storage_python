# Cache Storage

## Install

```bash
pip3 install cache-storage
```

## Usage

There are two adaptors (for now) for integrating with storage providers:
- DropboxClient
- LocalFileClient - for local development mostly

Each can be used as dependencies for the cache service.

```python
from cache_storage import Cache
from cache_storage import DropboxClient

TOKEN = "dropbox api token"

cache = Cache(DropboxClient(TOKEN))

# ./cache/ticker_{ticker}.json is the template fila path, ticker will be replaced with the function argument
# Setting 60 * 60 * 24 (1 day in seconds) as cache ttl
@cache.cache_factory("./cache/ticker_{ticker}.json", 60 * 60 * 24)
def test(ticker: str)-> dict:
    return {"test": True, "ticker": ticker}

if __name__ == "__main__":
    test("AAPL")
```


mihaiblebea@Mihais-MBP cache_storage % DROPBOX_TOKEN=sl.Bb9h5aVG8RbW5e0RyKB6y1q0s-qo27ZNDv6RAbAiwG9V1fQnlPcCiHRi0P__XEljwwFar9t1VFYddG5CNNWyBt7cMTTMUr4IaGbabyYZEw5IlPBJTGNBIPnJes0qjQuQbviqKAI ./execute.sh ./src/__init__.py
'sl.Bb8uaikFd6J-uIcZR-P035y8QdnmH9_50RfOXtGOtQRfufdiZWCdO3kmP7g2ZjFgMG6U1sWM3HLd6J7dTScp7phfdWWvHmEliqz2KPC6PvxfspxfofM2NBITd9uMnotFslIoquk'
'ae386k6Xto4AAAAAAAAAASjKjkqHYVe98phQ0rTti9epsqcLLelBIlrGwJZhiqEV'
datetime.datetime(2023, 4, 6, 17, 46, 31, 478832)
