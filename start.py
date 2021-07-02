from classes.database import DataBase
from classes.user import User
from classes.filesystem import FileSystem
from sys import argv

def main(argv):
    
    help_args = """
    -l - Output length you'r firstname and lastname.
    -h - Output help arguments.
    -c - Output current fistname and lastname.
    -a - Output all operations.
    """

    if argv[1] == "-l":

        firstname = input("Input firstname: ")
        lastname = input("Input lastname: ")
        if firstname and lastname:
            user = User(firstname, lastname)
            user.name_length()
        else:
            print("firstname or lastname is empty")

    elif argv[1] == "-c":

        firstname = input("Input firstname: ")
        lastname = input("Input lastname: ")
        if firstname and lastname:
            user = User(firstname, lastname)
            user.current_firstname_and_lastname()
        else:
            print("firstname or lastname is empty")
    
    elif argv[1] == "-a":
        
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

    elif argv[1] == "-h":
        print(help_args)
    else:
        print(help_args)

if __name__ == '__main__':
    main(argv)
    
