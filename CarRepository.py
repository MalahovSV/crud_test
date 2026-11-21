from models import Car
from storage import load_cars, save_cars

class CarRepository:
    def __init__(self) -> None:
        self.cars: list[Car] = load_cars()

    def _next_id(self) -> int:
        return max((c.id for c in self.cars), default=0) + 1

    def find_all(self) -> list[Car]:
        return list(self.cars)

    def find_by_id(self, car_id: int) -> Car | None:
        for car in self.cars:
            if car.id == car_id:
                return car
        return None

    def create (self, brand: str, model: str, year: int, price: float) -> Car | None:
        car = Car(self._next_id(), brand, model, year, price)
        if car in self.cars:
            raise ValueError("[ERROR]: такой же объект")
        self.cars.append(car)
        save_cars(self.cars)

    def update(self, 
               car_id: int,
               brand: str | None,
               model: str | None,
               year: int | None,
               price: float | None) -> bool:
        car = self.find_by_id(car_id)
        if car is None:
            return False

        if brand:
            car.brand = brand
        if model:
            car.model = model
        if year is not None:
            car.year = year
        if price is not None:
            car.price = price
        save_cars(self.cars)
        return True 

    def delete(self, car_id: int) -> bool:
        for i, car in enumerate(self.cars):
            if car.id == car_id:
                del self.cars[i]
                save_cars(self.cars)
                return True
        return False
    