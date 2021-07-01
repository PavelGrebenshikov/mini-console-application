from classes.database import DataBase
from classes.user import User
from classes.filesystem import FileSystem

def main():
    firstname = input("Input firstname: ")
    lastname = input("Input lastname: ")
    
    if firstname and lastname:
        # Classes
        user = User(firstname, lastname)
        DB = DataBase()
        filesys = FileSystem("user.txt")

        # functions

        DB.check_directory()
        user.name_length()
        user.past_name(filesys.read_file())
        filesys.create_file(data=user.validate())



    else:
        print("Вы ввели неверно")


if __name__ == '__main__':
    main()
    
