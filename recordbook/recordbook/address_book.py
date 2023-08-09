from collections import UserDict
from collections.abc import Iterator
from datetime import timedelta, datetime
import pickle

class AddressBook(UserDict):
       
    def add_record(self, record):
        self.data[record.name.value] = record
        return "1 record was successfully added - [bold green]success[/bold green]"
    
    def get_list_birthday(self, count_day: int):
        end_date = datetime.now() + timedelta(days=int(count_day))
        lst = [f"\nList of birthday before: {end_date.strftime('%d.%m.%Y')}"]
        for name, person in self.items():
            if not (person.birthday.value == "None"): 
                person_date = datetime.strptime(person.birthday.value, "%d.%m.%Y").date()
                person_month = person_date.month 
                person_day = person_date.day 
                dt = datetime(datetime.now().year, person_month, person_day) 
                if end_date >= dt > datetime.now(): 
                    lst.append(f"{name}|{person.birthday.value}|{', '.join(map(lambda phone: phone.value, person.phones))} - {person.days_to_birthday()}")
        return "\n".join(lst)

    # завантаження записів книги із файлу
    def load_database(self, path):
        with open(path, "rb") as fr_bin:
            self.data = pickle.load(fr_bin)  
                                                                    
        return f"The database has been loaded = {len(self.data)} records"
    
    # збереження записів книги у файл   
    def save_database(self, path):
        with open(path, "wb") as f_out:
            pickle.dump(self.data, f_out)
        return ""
            
    # генератор посторінкового друку
    def _record_generator(self, N=10):
        records = list(self.data.values())
        total_records = len(records)
        current_index = 0
        
        while current_index < total_records:
            batch = records[current_index: current_index + N]
            current_index += N
            yield batch

