def main():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 0:
            S += "B"
            N = N // 2
        else:
            S += "A"
            N -= 1
    print(S[::-1])

if __name__ == '__main__':
    main()