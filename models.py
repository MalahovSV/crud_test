from dataclasses import dataclass, asdict

@dataclass
class Car:
    id: int
    brand: str
    model: str
    year: int
    price: float

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "Car":
        return Car(
            id=data["id"],
            brand=data["brand"],
            model=data["model"],
            year=data["year"],
            price=data["price"]
        )
    def __eq__ (self, other: object) -> bool:
        if self is other:
            return True
        if not isinstance(other, Car):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __str__(self) -> str:
        return f'[{self.id}] {self.brand} {self.model} {self.year} - {self.price:.2f}'
    