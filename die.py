#################################################################################
#   Program Name: Dice Checker
#
#   Author: Lex Albrandt
#
#   Date: 06/14/25
#
#   File Name: die.py
#
#   Version: 1.0
#
#   File purpose: Initialize all functions for the die class
#################################################################################

import textwrap
import os
import time

class die:
    
    def __init__(self) -> None:
        """ Default constructor
        
            Returns: None
        """
        self._num_sides = 0
        self._num_samples = 0
        self._deg_free = 0
        self._valid_choice = False
        self._side_list = []


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

    
    def get_roll_entries(self) -> int:
        """ Function for the user to enter roll values
            for each side of the die
            
            Returns: None

            ValueError: invalid roll input, cannot be negative
        """

        total = 0
        self._side_list = [0] * (self._num_sides + 1)

        info = textwrap.dedent(f"""
        This section of the test will ask you to enter the number
        of rolls for each side of the die your are testing.""")
        print(info) 
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        for side in range(1, self._num_sides + 1):
            side_input = int(input(f"Enter the count for {side}: "))
            try:
                if side_input < 0:
                    self._valid_choice = False
                    raise ValueError("Number of rolls cannot be less than 0.")
                else:
                    self._valid_choice = True
                    
            except ValueError as e:
                print(f"Invalid input. {e}")

            while self._valid_choice == False:
                side_input = int(input(f"Enter the count for {side}: "))
                try:
                    if side_input < 0:
                        raise ValueError("Number of rolls cannot be less than 0.")
                    else:
                        self._valid_choice = True
                except ValueError as e:
                    print(f"Invalid input. {e}")
            self._side_list[side] = side_input
            total += side_input
        os.system('cls' if os.name == 'nt' else 'clear')
        
        return total