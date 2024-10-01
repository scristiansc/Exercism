"""
Functions used in preparing Guido's gorgeous lasagna.
1.bake_time_remaining
2.preparation_time_in_minutes
3.elapsed_time_in_minutes
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(actual_bake_time):
    """This function calculates the bake time remaining"""
    return EXPECTED_BAKE_TIME - actual_bake_time

    
def preparation_time_in_minutes(number_of_layers):
    """
    This function takes the number of layers you want to add to the lasagna as
    an argument and returns how many minutes you would spend making them.
    Assuming each layer takes 2 minutes to prepare.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """"This function has two parameters: 
    -number_of_layers (the number of layers added to the lasagna) -elapsed_bake_time (the number of minutes the lasagna has been baking in the oven). This function should return the total number of minutes you've been cooking"""
    prep_time = preparation_time_in_minutes(number_of_layers)
    total_time = prep_time + elapsed_bake_time
    return total_time