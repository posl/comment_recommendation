def get_next_prize():
    x = int(input())
    if x % 100 == 0:
        return 100
    else:
        return 100 - (x % 100)
print(get_next_prize())
