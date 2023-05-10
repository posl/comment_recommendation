def power_of_two(n):
    if n == 1:
        return True
    if n % 2 == 0:
        return power_of_two(n/2)
    else:
        return False
