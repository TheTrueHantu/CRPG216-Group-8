class Car:
    def __init__(self, car_id, name, make, body, year, value):
        self.car_id = car_id
        self.name = name
        self.make = make
        self.body = body
        self.year = year
        self.value = value
 
    def __str__(self):
        return f"{self.car_id}\t{self.name}\t{self.make}\t{self.body}\t{self.year}\t{self.value}"