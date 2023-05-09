def main():
    n = int(input())
    s = input()
    if n >= 1 and n <= 1000 and len(s) == n:
        print(s[-1])
    else:
        print('Invalid Input')
