def exchange_money(budget, exchange_rate):
     """
  Calculates the amount of exchanged currency based on the budget and exchange rate.
  Args:
    budget: The amount of money to be exchanged.
    exchange_rate: The amount of domestic currency equal to one unit of foreign currency.
  Returns:
    The value of the exchanged currency.
    """
     return budget / exchange_rate



def get_change(budget, exchanging_value):
    """
    :Arg budget: float - amount of money you own.
    :Arg exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value
   



def get_value_of_bills(denomination, number_of_bills):
    """
    :Arg denomination: int - the value of a bill.
    :Arg number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    return denomination * number_of_bills
    



def get_number_of_bills(amount, denomination):
    """
    :Arg amount: float - the total starting value.
    :Arg denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    return amount // denomination
    


def get_leftover_of_bills(amount, denomination):
    """
    :Arg amount: float - the total starting value.
    :Arg denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    return amount % denomination
    


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :Arg budget: float - the amount of your money you are planning to exchange.
    :Arg exchange_rate: float - the unit value of the foreign currency.
    :Arg spread: int - percentage that is taken as an exchange fee.
    :Arg denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    exchange = exchange_rate * spread / 100 + exchange_rate
    new_value = exchange_money(budget, exchange)
    number_bills = get_number_of_bills(new_value, denomination)
    return get_value_of_bills(denomination, number_bills)
