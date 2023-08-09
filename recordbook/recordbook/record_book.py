
from datetime import timedelta, datetime

from field import Name, Phone, Email, Birthday, Address
    
        
#========================================================
# Класс Record, который отвечает за логику 
#  - добавления/удаления/редактирования
# необязательных полей и хранения обязательного поля Name
#=========================================================
class Record():
    def __init__(self, name:Name, phones: Phone=None, email: Email=None, birthday: Birthday=None, address: Address=None) -> None:
        self.name = name            
        self.phones = [] 
        self.email = email
        self.birthday = birthday
        self.address = address
        self.phones.append(phones)
        
# ======================================================================================================
# =========================================[ add ]======================================================
# ======================================================================================================

    # Done - розширюємо існуючий список телефонів особи - Done
    # НОВИМ телефоном або декількома телефонами для особи - Done
    def add_phone(self, new_phone: Phone) -> str:
        self.phones.append(new_phone)
        return f"The phones was/were added - [bold green]success[/bold green]"
    

    def add_to_birthday(self, birthday:Birthday):
        self.birthday.value = birthday.value
        return ""

    def add_email(self, email:Email) -> None: 
        self.email.value = email.value
        return ""

    def add_address(self, address:Address) -> None: 
        self.address.value = ', '.join(address.value)
        return ""

# ======================================================================================================
# =========================================[ remove ]===================================================
# ======================================================================================================

    def remove_phone(self, phones:Phone, bool=True) -> str:
        if len(self.phones) == 0: return "This contact has no phone numbers saved"
        
        for n in self.phones:
            if n.value == phones.value:
                if bool:
                    if len(self.phones) == 1:
                        self.add_phone(Phone("None"))
                self.phones.remove(n)
                return phones

    def remove_birthday(self) -> None:
        self.birthday.value = "None"

    def remove_email(self) -> None: 
        self.email.value = "None"

    def remove_address(self) -> None: 
        self.address.value = "None"

# ======================================================================================================
# =========================================[ change ]===================================================
# ======================================================================================================

    def change_name(self, name:Name, new_name:Name) -> None: 
        if self.name.value == name.value: self.name = new_name

    def change_phone(self, old_phone:Phone, new_phone:Phone) -> str:
        for phones in self.phones:
            if str(old_phone) == str(phones):
                self.remove_phone(old_phone, False)
                self.add_phone(new_phone)
                return f"Phone {old_phone} change to {new_phone} for {self.name} contact "
        return f"Phone {old_phone} for contact {self.name} doesn`t exist"

    def change_birthday(self, new_birthday:Birthday) -> None:
        self.birthday = new_birthday

    def change_email(self, new_email:Email) -> None: 
        self.email = new_email

    def change_address(self, new_address:Address) -> None: 
        self.address.value = ' '.join(new_address.value)

    def __str__(self):
        return "{}{}{}{}{}".format(
                                   f"Name: {self.name}\n", 
                                   f'Phone: {", ".join([str(p) for p in self.phones]) if self.phones else "No phone"}\n', 
                                   'Email: ' + str(self.email.value) + "\n" if self.email is not "None" else "Email: No email\n",
                                   'Address: ' + str(self.address) + "\n" if self.address is not "None" else 'Address: No address\n',
                                   'Birthday: ' + str(self.birthday.value) + "\n" if self.birthday is not "None" else "Birthday: No birthday date\n")                       

    def __repr__(self):
        return "{}{}{}{}{}".format(
                                   f"Name: {self.name}\n", 
                                   f'Phone: {", ".join([str(p) for p in self.phones]) if self.phones else "No phone"}\n', 
                                   'Email: ' + str(self.email.value) + "\n" if self.email is not "None" else "Email: No email\n",
                                   'Address: ' + str(self.address) + "\n" if self.address is not "None" else 'Address: No address\n',
                                   'Birthday: ' + str(self.birthday.value) + "\n" if self.birthday is not "None" else "Birthday: No birthday date\n")                       


    # повертає кількість днів до наступного дня народження
    def days_to_birthday(self):
        if self.birthday.value:
            now_date = datetime.now()
            now_year = now_date.year
            
             # Определяем формат строки для Даты
            date_format = "%d.%m.%Y %H:%M:%S"
            # Строка с Датой народження
            date_string = f"{self.birthday.value} 00:00:00"  
            dt = datetime.strptime(date_string, date_format)
            
            birthday = datetime(day=dt.day, month=dt.month, year=now_year)
            
            if now_date > birthday:
                birthday = birthday.replace(year=now_date.year + 1)
                dif = (birthday - now_date).days
                return f"до {birthday.strftime('%d.%m.%Y')} залишилося = {dif}"
            else:
                dif = (birthday - now_date).days
                return f"до {birthday.strftime('%d.%m.%Y')} залишилося = {dif}"
        else: return f"We have no information about {self.name.value}'s birthday."
    
    # перевіряє наявність 1(одного)телефону у списку
    def check_dublicate_phone(self, search_phone: str) ->bool:  
        result = list(map(lambda phone: any(phone.value == search_phone), self.data[self.name.value].phones))
        return True if result else False
