from typing import Optional

import httpx

from .http import KarotterHTTP

__all__ = ("Karotter",)


class Karotter:
    def __init__(self, *, http: Optional[httpx.AsyncClient] = None):
        self.http = KarotterHTTP(http)
