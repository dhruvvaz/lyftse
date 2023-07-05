car1 = Car("Calliope", date(2021, 1, 1), 35000, 5000, False)
print(car1.needs_service())  # True
car2 = Car("Glissade", date(2021, 1, 1), 0, 0, True)
print(car2.needs_service())  # True
