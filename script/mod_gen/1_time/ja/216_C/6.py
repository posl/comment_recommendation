def main():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 0:
            N //= 2
            S = "B" + S
        else:
            N -= 1
            S = "A" + S
    print(S)

if __name__ == '__main__':
    main()