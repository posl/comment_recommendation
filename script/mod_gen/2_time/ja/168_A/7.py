def main():
    N = int(input())
    N = N % 10
    if N == 2 or N == 4 or N == 5 or N == 7 or N == 9:
        print("hon")
    elif N == 0 or N == 1 or N == 6 or N == 8:
        print("pon")
    elif N == 3:
        print("bon")

if __name__ == '__main__':
    main()