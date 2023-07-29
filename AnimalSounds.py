class Animal:
    def make_sound(self):
        print("__")

class Dog(Animal):
    def make_sound(self):
        print("Bark!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")

def animal_sound_in_zoo(animal):
    animal.make_sound()

def main():
    print("Animal Sounds in the Zoo:")
    print("--------------------------")
    
    dog = Dog()
    cat = Cat()
    
    print("Dog Sound in the Zoo:")
    animal_sound_in_zoo(dog)
    
    print("\nCat Sound in the Zoo:")
    animal_sound_in_zoo(cat)


if __name__ == "__main__":
    main()
