class Dog:
    def __init__(self, name, color, breed, emotion):
        self.name = name
        self.color = color
        self.breed = breed
        self.emotion = emotion

    def bark(self):
        print(self.name, "đang sủa gâu gâu!")

    def wag_tail(self):
        print(self.name, "đang vẫy đuôi")

    def eat(self):
        print(self.name, "đang ăn")

    def run(self):
        print(self.name, "đang chạy")
        
dog1 = Dog("Milu", "vàng", "Poodle", "vui")
print(dog1.bark())

class Car:
    def __init__(self, brand, size, color, price):
        self.brand=brand
        self.size=size
        self.color=color
        self.price=price
    def speed(self):
        print("xe tăng tốc")
    def brake(self):
        print("xe giảm tốc")
    def crash(self):
        print("xe đã đâm")

car = Car("bmw","sedan","black","3B")
print(car.speed())

class BankAccount:
    def __init__(self, name, account_number, bank, balance):
        self.name = name
        self.account_number = account_number
        self.bank = bank
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Đã gửi", amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Đã rút", amount)
        else:
            print("Không đủ tiền!")

    def check_balance(self):
        print("Số dư:", self.balance)


account = BankAccount("bien", "123456789", "tcb", 987654321)
account.withdraw(100000)
