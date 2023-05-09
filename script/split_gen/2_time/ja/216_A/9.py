def main():
    x = input()
    if float(x) >= 0 and float(x) <= 2:
        print(int(float(x)), end = '-')
    elif float(x) >= 3 and float(x) <= 6:
        print(int(float(x)), end = '')
    elif float(x) >= 7 and float(x) <= 9:
        print(int(float(x)), end = '+')
