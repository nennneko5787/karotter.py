from typing import Optional

import httpx

__all__ = ("KarotterHTTP",)


class KarotterHTTP:
    def __init__(self, http: Optional[httpx.AsyncClient] = None):
        self.http: httpx.AsyncClient = http or httpx.AsyncClient()
        self.http.base_url = "https://karotter.com/api/"
