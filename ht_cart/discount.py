class Discount:
    def __init__(self, value) -> None:
        if not isinstance(value, float):
            raise ValueError('Value must be a float')
        if not 0 <= value <= 1:
            raise ValueError('Value must be between 0 an 1')

        self._value = value

    def discount(self):
        raise NotImplementedError('Subclass must implement this method')
    

class RegularDiscount(Discount):
    def __init__(self, value=0.1) -> None:
        super().__init__(value)
        
    def discount(self):
        return self._value
    

class PremiumDiscount(Discount):
    def __init__(self, value=0.2) -> None:
        super().__init__(value)

    def discount(self):
        return self._value

