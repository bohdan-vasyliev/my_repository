class PriceError(Exception):
    
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f'PriceError: {self.message}'