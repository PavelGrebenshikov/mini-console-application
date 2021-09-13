from classes.database import DataBase
from classes.user import User
from classes.filesystem import FileSystem
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--lenght", help="Output length you'r firstname and lastname.", action="store_true")
    parser.add_argument("-c", "--current", help="Output current fistname and lastname", action="store_true")
    parser.add_argument("-a", "--all", help="Output all operations", action="store_true")
    args = parser.parse_args()

    if args.lenght:
        firstname = input("Input firstname: ")
        lastname = input("Input lastname: ")

        if firstname and lastname:
            user = User(firstname, lastname)
            user.name_length()
        else:
            print("firstname or lastname is empty")
    elif args.current:
        firstname = input("Input firstname: ")
        lastname = input("Input lastname: ")

        if firstname and lastname:
            user = User(firstname, lastname)
            user.current_firstname_and_lastname()
        else:
            print("firstname or lastname is empty")
    elif args.all:
        firstname = input("Input firstname: ")
        lastname = input("Input lastname: ")
        if firstname and lastname:
            user = User(firstname, lastname)
            filesys = FileSystem("user.txt")
            db = DataBase()
            user.name_length()
            user.past_name(filesys.read_file())
            user.current_firstname_and_lastname()
            db.check_directory()
            filesys.check_file()
            filesys.create_file(user.validate())
        else:
            print("firstname or lastname is empty")
    else:
        print("Show options -h or --help")
    

if __name__ == '__main__':
    main()

    
