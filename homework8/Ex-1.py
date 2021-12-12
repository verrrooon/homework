class Animals:
    def __init__(self, gender, name, age, species=0):
        self.gender = gender
        self.name = name
        self.age = age
        self.species = species

    def make_a_sound(self):
        print("Издаёт животный звук")

# Beast = Animals('female', 'Dysya', 2)
# print(Beast.name)
# print(Beast.age)
# Beast.make_a_sound()


class Mammals(Animals):
    def __init__(self, gender, name, age, species):
        super().__init__(gender, name, age, species)

    def feeding(self):
        print('Кормлю детей молоком')


class Human(Mammals):
    def __init__(self, gender, name, age, species, marital_status, job):
        super().__init__(gender, name, age, species)
        self.marital_status = marital_status
        self.job = job

    def info(self):
        print(f'Меня зовут {self.name}. Моя профессия - {self.job}.')

    def status(self):
        print(f'На данный момент я {self.marital_status}.')

    def goToJob(self):
        print('Я иду на работу!')

# Tom = Human('male', 'Tom', 22, 'человек', 'свободен', 'программист')
# Tom.info()
# Tom.status()
# Tom.goToJob()


class Cat(Mammals):
    def __init__(self, gender, name, age, species, breed):
        super().__init__(gender, name, age, species)
        self.breed = breed

    def info(self):
        print(f'Приветствую тебя, мой раб! Меня зовут {self.name}.')

    def make_sound(self):
        print('Мяяяяяу!')


# Barsik = Cat('male', 'Barsik', 7, 'кот', 'мейн-кун')
# Barsik.info()
# Barsik.make_sound()


class Dog(Mammals):
    def __init__(self, gender, name, age, species, breed):
        super().__init__(gender, name, age, species)
        self.breed = breed

    def info(self):
        print(
            f'Меня зовут {self.name}. Я жду, пока ты кинешь мне тенисный мячик, чтобы принести тебе его обратно!')

    def make_sound(self):
        print('Гав-гав!')

    def dig(self):
        print('Я хочу прокопать землю насквозь')


# Gerda = Dog('female', 'Gerda', 14, 'собака', 'далматин')
# Gerda.info()
# Gerda.make_sound()
