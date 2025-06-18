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
import scipy.stats as stats

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
        self._chi_squared_value = 0
        self._expected_freq = 0
        self._observed_value = 0
        self._p_value = 0
        self._significance_level = 0.05


    def get_sides(self) -> None:
        """ Function to get the number of sides for the die the user wants to test
        
            Raises:
                ValueError: for invalid number of sides

            Returns: None
        """ 

        while not self._valid_choice:
            try:
                self._num_sides = int(input("How many sides does your die have: "))
                if self._num_sides not in range(4, 21):
                    raise ValueError("Number of sides cannot be less than 4 or greater than 20")

                self._valid_choice = True
                self._deg_free = self._num_sides - 1
                if self._num_sides == 4:
                    self._num_samples = self._num_sides * 5
                else:
                    self._num_samples = self._deg_free * self._num_sides
                self._expected_freq = self._num_samples // self._num_sides
            except ValueError as e:
                print(f"Invalid input. {e}")

        print(f"\nThe number of rolls you need to perform for your die with {self._num_sides} sides is {self._num_samples}.")
        time.sleep(5)


    def print_initial_info(self) -> None:
        """ Function to print out the info based on user input

            Returns: None
        """

        info = textwrap.dedent(f"""
        Here is the info for your test:
        ---------------------------------
        Number of sides:        {self._num_sides}
        Degrees of Freedom:     {self._deg_free}
        Number of samples:      {self._num_samples}
        Expected Frequency:     {self._expected_freq}""")
        print(info)
        time.sleep(5)

    
    def get_roll_entries(self) -> None: 
        """ Function for the user to enter roll values
            for each side of the die
            
            Returns: None

            ValueError: invalid roll input, cannot be negative
        """

        total = 0
        self._side_list = [0] * (self._num_sides + 1)

        while total < self._num_samples:
            total = 0

            info = textwrap.dedent(f"""
            The next section of the test will ask you to enter the number
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
            if total < self._num_samples:
                print(f"You only rolled the die {total} times. You must roll the die\n"
                      f"{self._num_samples} times for the test to be valid. Please check your\n"
                      "results and try again")
        
        return
    
    
    def compute_chi_squared(self) -> None:
        """ Function to compute the chi squared value for a given die
        
            Returns: None
        """
        self._chi_squared_value = 0

        for i in range(1, self._num_sides + 1):
            observed_value = self._side_list[i]
            self._chi_squared_value += ((observed_value - self._expected_freq) ** 2) / self._expected_freq

        print(f"Chi-squared value: {self._chi_squared_value}")

    
    def is_fair(self) -> None:
        self._p_value = 1 - stats.chi2.cdf(self._chi_squared_value, self._deg_free)
        print(f"p-value: {self._p_value}")
        if self._p_value < self._significance_level:
            print("Not fair")