from collections import UserDict
from datetime import datetime
import json

class Tag:
    def __init__(self, value=None):        
        self.__value = None
        self.value = value
        
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value:
            self.__value = value

class Note(Tag):
    pass

class NoteRecord():    
    def __init__(self, key: str, note: Note=None, tag: Tag=None):        
        self.key = str(datetime.now().replace(microsecond=0).timestamp())
        self.note = note
        self.tag = tag

    def __str__(self):
        return f"{str(self.key)} {str(self.note if self.note else '')} {str(self.tag if self.tag else '')}"
    
    def __repr__(self):
        return f"{str(self.key)} {str(self.note if self.note else '')} {str(self.tag if self.tag else '')}"
                
    def add_note(self, note: Note):
        self.note = note
        return f"Note {note} added."

    def del_note(self, note):
        self.note = None
        return f"Note {note} deleted"

    def change_note(self, old_note: Note, new_note: Note, tag: Tag):
        self.del_note(old_note)
        self.add_note(new_note)
        self.tag = tag
        #return f"Note {old_note} was replaced by {new_note} with tag {self.tag}"
        return f"\nDeleted note: {old_note}\nNew note: {new_note}\nNew Tag: {self.tag}"

class NoteBook(UserDict):
    def add_record(self, record: NoteRecord):
        self.data[record.key] = record
        return f"Added new record {record}"
    
    def del_record(self, record: NoteRecord):
        result = self.data.pop[record.key]
        return f"Record {result} deleted"
        
    def iterator(self, group_size=15):
        records = list(self.data.values())
        self.current_index = 0

        while self.current_index < len(records):
            group_items = records[self.current_index:self.current_index + group_size]
            group = [rec for rec in group_items]
            self.current_index += group_size
            yield group

    def save_data(self, filename):
        with open(filename, 'w') as f:

            json.dump({str(record.key): (str(record.note  if record.note else ""), str(record.tag if record.tag else "")) for key, record in self.items()}, f, indent=4)

        return f"The note_book is saved."

    def load_data(self, filename):
        try:
            with open(filename, 'r') as f:
                data_dict = json.load(f)
                for key, value in data_dict.items():                    
                    note, tag = value
                    note = Note(note)
                    tag = Tag(tag)
                    record = NoteRecord(key, note, tag)
                    self.data[record.key] = record

            if isinstance(self.data, dict):
                print(f"The note_book is loaded.")
            else:
                print("The file does not contain a valid note_book.")
        except FileNotFoundError:
            print(f"The file {filename} does not exist")


    def find_note(self, fragment:str):
        count = 0
        result = ""
        for rec in self.values():
            line = str(rec) + "\n"
            if fragment in line.lower():
                result += line
                count += 1
        if result:
            #result = f"The following {str(count)} records were found on the fragment '{fragment}' \n\n" + result
            result = f"\nSearch result {str(count)} records:\nNotes:\n{result}Search string: {fragment}"
        else:
            result = f"No records was found for the fragment '{fragment}' \n"
        return result
    
if __name__ == "__main__":

    nb = NoteBook()
    file_name = "n_book.json"
    print(nb.load_data(file_name))
    print(nb) 

    key=datetime.now().replace(microsecond=0).timestamp()
    note = Note('Create tag sorting')
    rec = NoteRecord(key, note, Tag('Project'))
    nb.add_record(rec)

    print(nb.find_note('note'))
    print(nb.save_data(file_name))
    print(nb)