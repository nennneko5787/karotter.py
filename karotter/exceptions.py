class KarotterBaseError(Exception):
    def __init__(self, statusCode: int, message: str):
        super().__init__(f"Karotter {statusCode} error: {message}")
        self.statusCode: int = statusCode
        self.message: str = message


class KarotterServerError(KarotterBaseError):
    pass


class KarotterClientError(KarotterBaseError):
    pass
