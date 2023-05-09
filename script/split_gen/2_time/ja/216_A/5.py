def main():
    x = input()
    y = int(x[-1])
    if 0 <= y <= 2:
        print(x[:-2] + '-')
    elif 3 <= y <= 6:
        print(x[:-2])
    elif 7 <= y <= 9:
        print(x[:-2] + '+')
