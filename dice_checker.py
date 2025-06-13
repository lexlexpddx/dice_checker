import textwrap
from Menu import Menu
from Compute import Compute
    
        
def main():
    my_compute = Compute()
    menu = Menu()
    user_choice = -1
    
    menu.print_welcome()
    menu.print_description()
    while user_choice != 3:
        menu.print_menu()
        try:
            user_choice = menu.get_user_choice()
            if user_choice == -1:
                raise ValueError
            if user_choice == 1:
                print(f"Test here")
                my_compute.get_info()
                my_compute.print_initial_info()
            if user_choice == 2:
                print(f"Results here")

        except ValueError as error:
            print(f"Invalid input. Menu choice must be between 1 and 3. Try again.\n")
        
    menu.print_exit()

    
    
    
    
if __name__ == "__main__":
    main()