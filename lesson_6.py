# -*- coding: utf-8 -*-

# exercise 1. Светофор

from time import sleep 
class TrafficLight:
    __color = {1: "Красный", 2: "Желтый", 3:"Зеленый"} 
    def running(self, n): 
        print(TrafficLight.__color[n]) 
svetofor = TrafficLight()
lighttime = {1: 7, 2: 2, 3: 4} 
while True: 
    for el in range(1,4): 
        svetofor.running(el) 
        sleep(lighttime[el])


# exercise 2. Масса асфальта
class Road:
    def __init__(self, _length, _width):
        self.length = _length
        self.width = _width
    def calc(self):
        weight = 200
        thick = 5
        usage = self.length * self.width * weight * thick
        print(f"Масса асфальта составляет: {usage} кг")

volume = Road(15, 3000)
volume.calc()


# exercise 3. Зарплаты 

class Worker:
    wage = {'Seller': 30000, 'Driver': 60000, 'Manager': 90000}
    bonus = {'Seller': 30000, 'Driver': 5000, 'Manager': 20000}
    _income = {'wage': wage, 'bonus': bonus}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        print(f"Employee {self.name} {self.surname}")

    def _get_total_income(self):
        a = Position._income.get('wage').get(self.position)
        b = Position._income.get('bonus').get(self.position)
        
petr = Position('Eduard', 'Rastlevsky', 'Seller')
petr.get_full_name()
petr._get_total_income()

# exercise 4. Движение автомобиля

class Car:

    def __init__(self, name, speed = 30, is_police=False):
        self.name = name
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f" Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self):
        print(f"Машина повернула")
        
    def show_speed(self):
        print('Cкорость автомобиля составляет {self.speed} км/ч')

class TownCar(Car):

    def __init__(self, name,speed):
        super().__init__(name,speed)

    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена')


class SportCar(Car):

    def __init__(self, name):
        super().__init__(name)

class WorkCar(Car):

    def __init__(self, name):
        super().__init__(name)

    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена')


class PoliceCar(Car):

    def __init__(self, name, is_police=True):
        super().__init__(name, is_police)
        
gazel = WorkCar('Газель')
gazel.go()
gazel.show_speed()
ferrari = SportCar('Ferrari')
ferrari.go()
ferrari.show_speed()
ferrari.stop()
print()
opel = TownCar('Опель',30)
opel.go()
opel.show_speed()
print()
uaz = PoliceCar('Уазик')
uaz.go()
uaz.show_speed()
print()


# exercise 5.Рисование

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки c помощью {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки c помощью {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки c помощью {self.title}")

pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Фломастер')
handle.draw() 

