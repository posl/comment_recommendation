def main():
    n = int(input())
    if n < 11:
        print(0)
    elif n < 111:
        print(9)
    elif n < 1111:
        print(9 + 10)
    elif n < 11111:
        print(9 + 10 + 100)
    elif n < 111111:
        print(9 + 10 + 100 + 1000)
    elif n < 1111111:
        print(9 + 10 + 100 + 1000 + 10000)
    elif n < 11111111:
        print(9 + 10 + 100 + 1000 + 10000 + 100000)
    elif n < 111111111:
        print(9 + 10 + 100 + 1000 + 10000 + 100000 + 1000000)
    elif n < 1111111111:
        print(9 + 10 + 100 + 1000 + 10000 + 100000 + 1000000 + 10000000)
    elif n < 11111111111:
        print(9 + 10 + 100 + 1000 + 10000 + 100000 + 1000000 + 10000000 + 100000000)
    else:
        print(9 + 10 + 100 + 1000 + 10000 + 100000 + 1000000 + 10000000 + 100000000 + 1000000000)