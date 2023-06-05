def withdraw(amount):
    if amount == 0:
        return 0
    result = 100000
    for i in range(1, 100000):
        if amount >= i**6:
            result = min(result, withdraw(amount-i**6)+1)
        if amount >= i**9:
            result = min(result, withdraw(amount-i**9)+1)
    return result
print withdraw(int(raw_input()))
