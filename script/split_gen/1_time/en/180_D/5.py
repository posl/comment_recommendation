def main():
    str_exp = input().split()
    str_exp = [int(i) for i in str_exp]
    x = str_exp[0]
    y = str_exp[1]
    a = str_exp[2]
    b = str_exp[3]
    exp = 0
    while x * a <= x + b and x * a < y:
        x = x * a
        exp += 1
    exp += (y - x - 1) // b
    print(exp)
