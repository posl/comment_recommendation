def main():
    N = int(input())
    S = ""
    while N > 0:
        if N%2 == 0:
            S = "B" + S
            N = N//2
        else:
            S = "A" + S
            N = N-1
    print(S)

if __name__ == '__main__':
    main()