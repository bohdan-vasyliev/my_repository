class Discount:
    def __init__(self, value) -> None:
        if not isinstance(value, float):
            raise TypeError('Value must be a float')
        if not 0 <= value <= 1:
            raise ValueError('Value must be between 0 an 1')
    
        self.value = value

    def discount():
        raise NotImplementedError('Subclass must implement this method')
    

class SilverDiscount(Discount):
    def __init__(self, value=0.1) -> None:
        super().__init__(value)

    def discount(self):
        return self.value
    

class GoldenDiscount(Discount):
    def __init__(self, value=0.3) -> None:
        super().__init__(value)

    def discount(self):
        return self.value