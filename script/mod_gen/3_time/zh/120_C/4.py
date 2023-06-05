def main():
    S = input()
    N = len(S)
    c = 0
    for i in range(N):
        if S[i] == "0":
            c += 1
        else:
            c -= 1
    print(N - abs(c))

if __name__ == '__main__':
    main()