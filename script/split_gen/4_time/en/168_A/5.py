def main():
    n = int(input())
    n = n % 10
    if n == 2 or n == 4 or n == 5 or n == 7 or n == 9:
        print('hon')
    elif n == 0 or n == 1 or n == 6 or n == 8:
        print('pon')
    elif n == 3:
        print('bon')
