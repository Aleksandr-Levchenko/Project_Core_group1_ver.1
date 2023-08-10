from record_classes import PhoneException, BirthdayException, EmailException




# Декоратор для Обробки командної строки
def input_error(func):
    def inner(*args):
        try:
            result = func(*args) 
            # if not result == "Good bye!": 
            #     return result
            # else: 
            return result   
        
        # Обробка виключних ситуацій
        except BirthdayException as e:
            print(e)
        except PhoneException as e:
            print(e)
        except EmailException as e:
            print(e)
        except FileNotFoundError:    # Файл бази даних Відсутній
            print("The database isn't found")
        except ValueError:
            print("Incorect data or unsupported format while writing to the file")
        except KeyError:
            print("Record isn't in the database")                 
        except TypeError:
            print("Incorect data")
    return inner
