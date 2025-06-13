import textwrap

class Menu:
    
    def __init__(self):
        pass
    
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
        result = int(input(f"Please make a menu choice: "))
        if result == 3:
            while quit != 'y' or quit != 'n':
                try:
                    quit = input("Are you sure you want to quit (y/n): ")
                    if quit != 'y' and quit != 'n':
                        raise ValueError
                    if quit == 'y':
                        return 3
                    else:
                        return 0
                except ValueError:
                    print("Invalid input. Please enter 'y' or 'n'.")
            
        if result < 1 or result > 3:
            return -1

        return result 