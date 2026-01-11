from datetime import datetime


class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date          # приватный
        self.__occupation = occupation          # приватный
        self.__higher_education = higher_education  # приватный

    # --- occupation ---
    @property
    def occupation(self):
        return self.__occupation

    # --- higher_education ---
    @property
    def higher_education(self):
        return self.__higher_education

    # --- age ---
    @property
    def age(self):
        birth = datetime.strptime(self.__birth_date, "%d.%m.%Y")
        today = datetime.today()
        age = today.year - birth.year

        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1
        return age

    def introduce(self):
        edu_text = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.occupation}. "
            f"У меня {edu_text}."
        )


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        edu_text = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.occupation}. "
            f"Я учился с Сезим в группе {self.group}. "
            f"У меня {edu_text}."
        )


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        edu_text = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.occupation}. "
            f"Мое хобби {self.hobby}. "
            f"У меня {edu_text}."
        )


# --- Проверка ---
cl1 = Classmate("Нуртай", "20.02.2003", "Юрист", True, "11A")
cl1.introduce()

fr1 = Friend("Байэл", "01.03.2002", "Дизайнер", True, "Бокс")
fr1.introduce()
print(fr1.age)
