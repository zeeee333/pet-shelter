class Pet:
"""A basic pet. Every pet has a name, an age, and some energy."""
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.energy = 3
  def speak(self):
    return "..."
  def play(self):
    if self.energy > 0:
      self.energy -= 1
      return f"{self.name} plays happily! Energy left: {self.energy}"
    return f"{self.name} is too tired to play."
  def describe(self):
    return f"{self.name} is {self.age} years old and says {self.speak()}"
  def sleep(self):
    self.energy = 3
    return f"{self.name} takes a nap. Energy is back to {self.energy}."

class Dog(Pet):
  def speak(self):
    return "Woof!"

class Cat(Pet):
  def speak(self):
    return "Hiss!"
    
class Bird(Pet):
  def __init__(self, name, age, can_fly=True):
    super().__init__(name, age)
    self.can_fly = can_fly
    self.energy = 5

  def speak(self):
    return "Tweet!"
  def describe(self):
    flying = "can fly" if self.can_fly else "cannot fly"
    return super().describe() + f" and {flying}."
  
