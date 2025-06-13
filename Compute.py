import textwrap

class Compute:

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