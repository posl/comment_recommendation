def main():
    P = list(map(int, input().split()))
    S = ""
    for i in range(1, 27):
        S += chr(ord("a") + P.index(i))
    print(S)

if __name__ == '__main__':
    main()