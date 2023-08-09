import re
from datetime import timedelta, datetime
from bot_exception import EmailException, PhoneException, BirthdayException


# батьківський клас
class Field():
    def __init__(self, value) -> None:
        self.__value = None
        self.value = value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return str(self.value)
    
# клас Ім'я
class Name(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value

  
# клас Телефон
class Phone(Field): 
    @property
    def value(self):
        return self.__value 
    
    @value.setter
    def value(self, value):
        if value.lower() == "none": 
            self.__value = "None"
            return ""   # не видаляти
        
        if value:
            correct_phone = ""
            for i in value: 
                if i in "+0123456789": correct_phone += i

            if len(correct_phone) == 13: self.__value = correct_phone # "+380123456789"
            elif len(correct_phone) == 12: self.__value = "+" + correct_phone # "380123456789"
            elif len(correct_phone) == 10: self.__value = "+38" + correct_phone # "0123456789"
            elif len(correct_phone) == 9: self.__value = "+380" + correct_phone # "123456789"
            else: raise PhoneException("Incorrect phone format")   # невірний формат телефона

    
# клас День народження        
class Birthday(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value:str):
        if value.lower() == "none": 
            self.__value = "None"
        else:
            value = re.sub("[-/]", ".", value)
            _ = datetime.strptime(value, "%d.%m.%Y")

            pattern = r"^\d{2}(\.|\-|\/)\d{2}\1\d{4}$"  # дозволені дати формату DD.MM.YYYY 
            if re.match(pattern, value):         # альтернатива для крапки: "-" "/"
                self.__value = value  # комбінувати символи ЗАБОРОНЕНО DD.MM-YYYY 

class Address(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value

  
class Email(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if value.lower() == "none": 
            self.__value = "None"
        else:
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(pattern, value):
                raise EmailException("Invalid email address!")
            else:
                self.__value = value 