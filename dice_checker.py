import textwrap
from Menu import Menu

class compute:

    num_sides = 0
    num_samples = 0
    deg_free = 0
    text_input = 'y'
    int_input = 0
    valid_choice = False
    
    def __init__(self):
        pass    

    def get_info(self) -> None:
        self.num_sides = int(input("How many sides does your die have: "))
        self.deg_free = self.num_sides - 1
        self.num_samples = self.deg_free * self.num_sides
        print(f"The minimum number of rolls for your die with {self.num_sides} sides is {self.num_samples}.")

        while not self.valid_choice:
            try:
                self.text_input = input("Would you like to use this number (y/n): ")
                if self.text_input not in ['y', 'n']:
                    raise ValueError("Must enter 'y' or 'n'")

                if self.text_input == 'n':
                    self.int_input = int(input(f"Ok. How many samples would you like to include (must be greater than {self.num_samples}): "))
                    if self.int_input < self.num_samples:
                        raise ValueError(f"Must be greater than {self.num_samples}")
                    self.num_samples = self.int_input

                self.valid_choice = True

            except ValueError as e:
                print(f"Invalid input: {e}")

    def print_initial_info(self) -> None:
        info = textwrap.dedent(f"""
        Here is the info for your test:
        ---------------------------------
        Number of sides:        {self.num_sides}
        Degrees of Freedom:     {self.deg_free}
        Number of samples:      {self.num_samples}""")
        print(info)
    

# class Menu:
    
#     def __init__(self):
#         pass
    
#     def print_welcome(self) -> None:
#         welcome = textwrap.dedent("""
#             Welcome to the Dice Checker! This program will help you determine if your new
#             set of dice is fairly weighted.""")
#         print(welcome)
    
#     def print_description(self) -> None:
#         description = textwrap.dedent("""
#             The program uses the Pearson's chi-square test from statistics that computes
#             a number that indicates the probability that the sides of the die are rolled
#             randomly. If you would like more info on the test here is the Wikipedia page:

#             https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test

#             There is also a blog post detailing the process at:

#             https://deltasdnd.blogspot.com/2009/02/testing-balanced-die.html?m=1

#             Let's start testing your new dice!""")
#         print(description)

#     def print_menu(self) -> None:
#         menu = textwrap.dedent("""
#               Menu
#               ---------------------------------
#               1. Start test
#               2. See results
#               3. Quit
#               """)
#         print(menu)
    
#     def print_exit(self) -> None:
#         print(f"Thanks for using the Dice Checker! Happy rolling!")

#     def get_user_choice(self) -> int:
#         quit = 't'
#         result = int(input(f"Please make a menu choice: "))
#         if result == 3:
#             while quit != 'y' or quit != 'n':
#                 try:
#                     quit = input("Are you sure you want to quit (y/n): ")
#                     if quit != 'y' and quit != 'n':
#                         raise ValueError
#                     if quit == 'y':
#                         return 3
#                     else:
#                         return 0
#                 except ValueError:
#                     print("Invalid input. Please enter 'y' or 'n'.")
            
#         if result < 1 or result > 3:
#             return -1

#         return result 
        
def main():
    my_compute = compute()
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