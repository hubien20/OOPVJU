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
