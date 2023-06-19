def func(n):
    for i in range(1,10):
        if n % i == 0 and n / i <= 9:
            return "Yes"
    return "No"
