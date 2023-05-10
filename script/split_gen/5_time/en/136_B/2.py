def main():
    N = int(input())
    if N < 10:
        print(N)
    elif N < 100:
        print(9)
    elif N < 1000:
        print(9 + N - 99)
    elif N < 10000:
        print(9 + 900)
    elif N < 100000:
        print(9 + 900 + N - 9999)
    else:
        print(9 + 900 + 90000)
