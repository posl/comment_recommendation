def calc_happy(x):
    happy = 0
    happy += int(x / 500) * 1000
    x = x - int(x / 500) * 500
    happy += int(x / 5) * 5
    return happy
x = int(input())
print(calc_happy(x))
