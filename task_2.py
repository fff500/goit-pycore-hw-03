import random

def get_numbers_ticket(min, max, quantity):
    if type(min) != int or type(max) != int or type(quantity) != int \
    or quantity < 1 or quantity > max - min:
        return []
  
    return sorted(random.sample(range(min, max), quantity))
