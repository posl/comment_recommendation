def main():
    N = int(input())
    if N < 1000:
        print(0)
    elif N < 1000000:
        print(N-999)
    elif N < 1000000000:
        print(999000 + (N-999999)*2)
    elif N < 1000000000000:
        print(999000000 + (N-999999999)*3)
    else:
        print(999000000000 + (N-999999999999)*4)
main()
