def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N = sorted(N)
    N = N[::-1]
    N = [str(i) for i in N]
    N = ''.join(N)
    N = int(N)
    if N % 3 == 0:
        print(0)
    else:
        if N % 3 == 1:
            if N % 10 == 1 or N % 10 == 4 or N % 10 == 7:
                print(1)
            elif N % 100 == 61 or N % 100 == 31 or N % 100 == 91:
                print(2)
            elif N % 1000 == 361 or N % 1000 == 631 or N % 1000 == 901:
                print(3)
            elif N % 10000 == 9361 or N % 10000 == 9631 or N % 10000 == 9901:
                print(4)
            elif N % 100000 == 99361 or N % 100000 == 99631 or N % 100000 == 99901:
                print(5)
            elif N % 1000000 == 999361 or N % 1000000 == 999631 or N % 1000000 == 999901:
                print(6)
            elif N % 10000000 == 9999361 or N % 10000000 == 9999631 or N % 10000000 == 9999901:
                print(7)
            elif N % 100000000 == 99999361 or N % 100000000 == 99999631 or N % 100000000 == 99999901:
                print(8)
            elif N % 1000000000 == 999999361 or N % 1000000000 == 999999631 or N % 1000000000 == 999999901:
                print(9)
            elif N % 10000000000 == 9999999361 or N % 10000000000 == 9999999631 or N % 10000000000 == 9999999901:
                print(10)
            elif N % 100000000000 == 99999999361 or N %

if __name__ == '__main__':
    main()