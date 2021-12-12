class Human:
    def __init__(self, gender, name, age, marital_status, job):
        self.gender = gender
        self.name = name
        self.age = age
        self.marital_status = marital_status
        self.job = job

    def info(self):
        print(f'Меня зовут {self.name}. Моя профессия - {self.job}.')

    def status(self):
        print(f'На данный момент я {self.marital_status}.')

    def goToJob(self):
        print('Я иду на работу!')


class Student(Human):
    def __init__(self, gender, name, age, number_of_dz_delivered, marital_status=0, job=0):
        super().__init__(gender, name, age, marital_status, job)
        self.number_of_dz_delivered = number_of_dz_delivered

    def homework(self):
        print(
            f'Меня зовут {self.name}. Я сдал {self.number_of_dz_delivered} домашних  работ')


# Tim = Student('мужской', 'Тимофей', 21, 12)
# Tim.homework()
