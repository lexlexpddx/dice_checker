#################################################################################
#   Program Name: Dice Checker
#
#   Author: Lex Albrandt
#
#   Date: 06/13/25
#
#   File Name: Compute.py
#
#   Version: 1.0
#
#   File purpose: Initializes all function associated with the Compute class
#################################################################################

import textwrap

class Compute:
    
    def __init__(self):
        """ Default constructor
        
            Returns: None
        """
        self._num_sides = 0
        self._num_samples = 0
        self._deg_free = 0
        self._expect_freq = 0   
        self._text_input = ''
        self._int_input = 0
        self._valid_choice = False


    def get_info(self) -> None:
        """ Wrapper function to get dice info from user

            Returns: None
        """
        self.get_sides()
        self.get_sample_size()


    def get_sides(self) -> None:
        """ Function to get the number of sides for the die the user wants to test
        
            Raises:
                ValueError: for invalid number of sides

            Returns: None
        """ 

        while not self._valid_choice:
            try:
                self._num_sides = int(input("How many sides does your die have: "))
                if self._num_sides not in range(1, 21):
                    raise ValueError("Number of sides cannot be less than 1 or greater than 20")

                self._valid_choice = True
                self._deg_free = self._num_sides - 1
                self._num_samples = self._deg_free * self._num_sides
            except ValueError as e:
                print(f"Invalid input. {e}")

        print(f"The number of rolls you need to perform for your die with {self._num_sides} sides is {self._num_samples}.")



    def print_initial_info(self) -> None:
        """ Function to print out the info based on user input

            Returns: None
        """

        info = textwrap.dedent(f"""
        Here is the info for your test:
        ---------------------------------
        Number of sides:        {self._num_sides}
        Degrees of Freedom:     {self._deg_free}
        Number of samples:      {self._num_samples}""")
        print(info)