import CarRepository

def prompt(msg: str):
    return input(msg).strip()


def prompt_int(msg: str) -> int | None:
    value = prompt(msg)
    if not value:
        return None
    try:
        return int(value)
    except ValueError:
        print("Need int")
        return None

def prompt_float(msg: str) -> float | None:
    value = prompt(msg)
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        print("Need float")
        return None

def menu() -> None:
    repo = CarRepository() # pyright: ignore[reportCallIssue]

    while True:
        print('\n-------MENU--------\n')
        print('1. Show all cars')
        print('2. Add car')
        print('3. Update car')
        print('4. Delete car')
        print('0. Exit')

        choice = prompt("Choice: ")

        if choice == "1":
            cars = repo.find_all()
            if not cars:
                print('list is empty')
            for car in cars:
                print(car)

        elif choice == 2:
            brand = prompt("Mark: ")
            model = prompt("Model: ")
            year = prompt_int("Year: ")
            price = prompt_float("Price: ")
            if year is None or price is None:
                print("Don`t correct data")
                continue
            try:
                car = repo.create(brand, model, year, price)
                print(f"Added: {car}")
            except ValueError as e:
                print(f"[ERROR]: {e}")

        elif choice == "3":
            car_id = prompt_int("Select id car: ")
            if car_id is None:
                continue
            brand = prompt('New mark (Enter - skip): ') or None
            model = prompt('New model (Enter - skip): ') or None
            year = prompt('New year (Enter - skip): ')
            price = prompt_float("New price (Enter - skip): ")
            if repo.update(car_id, brand, model, year, price):
                print("updated")
            else:
                print("Exception")

        elif choice == "4":
            car_id = prompt_int("ID car for delete record: ")
            if car_id is None:
                continue

            if repo.delete(car_id):
                print("deleted")
            else:
                print("Exception")

        elif choice == "0":
            print('Bye')
            break
        else:
            print("unknow command")

if __name__ == '__main__':
    menu()