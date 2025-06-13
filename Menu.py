import textwrap

class Menu:

    def __init__(self):
        self.user_choice = 0
        self.quit_choice = ''
    
    def print_welcome(self) -> None:
        welcome = textwrap.dedent("""
            Welcome to the Dice Checker! This program will help you determine if your new
            set of dice is fairly weighted.""")
        print(welcome)
    
    def print_description(self) -> None:
        description = textwrap.dedent("""
            The program uses the Pearson's chi-square test from statistics that computes
            a number that indicates the probability that the sides of the die are rolled
            randomly. If you would like more info on the test here is the Wikipedia page:

            https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test

            There is also a blog post detailing the process at:

            https://deltasdnd.blogspot.com/2009/02/testing-balanced-die.html?m=1

            Let's start testing your new dice!""")
        print(description)

    def print_menu(self) -> None:
        menu = textwrap.dedent("""
              Menu
              ---------------------------------
              1. Start test
              2. See results
              3. Quit
              """)
        print(menu)
    
    def print_exit(self) -> None:
        print(f"Thanks for using the Dice Checker! Happy rolling!")

    def get_user_choice(self) -> int:
        quit = 't'
        self.user_choice = int(input(f"Please make a menu choice: "))
        if self.user_choice == 3:
            while self.quit_choice != 'y' or self.quit_choice != 'n':
                try:
                    self.quit_choice = input("Are you sure you want to quit (y/n): ")
                    if self.quit_choice != 'y' and self.quit_choice != 'n':
                        raise ValueError
                    if self.quit_choice == 'y':
                        return 3
                    else:
                        return 0
                except ValueError:
                    print("Invalid input. Please enter 'y' or 'n'.")
            
        if self.user_choice < 1 or self.user_choice > 3:
            return -1

        return self.user_choice 


    # def execute_menu(self) -> None:
    #     self.print_welcome()
    #     self.print_description()
    #     while self.user_choice != 3:
    #         self.print_menu()
    #         try:
    #             self.user_choice = self.get_user_choice()
    #             if self.user_choice == -1:
    #                 raise ValueError
    #             if self.user_choice == 1:
    #                 print(f"Test here")
    #                 my_compute.get_info()
    #                 my_compute.print_initial_info()
    #             if self.user_choice == 2:
    #                 print(f"Results here")

    #         except ValueError as error:
    #             print(f"Invalid input. Menu choice must be between 1 and 3. Try again.\n")
            
    #     self.print_exit()
