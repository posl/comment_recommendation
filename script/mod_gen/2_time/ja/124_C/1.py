def main():
    S = input()
    N = len(S)
    c0 = 0
    c1 = 0
    for i in range(N):
        if i % 2 == 0:
            if S[i] == "0":
                c0 += 1
            else:
                c1 += 1
        else:
            if S[i] == "0":
                c1 += 1
            else:
                c0 += 1
    print(min(c0, c1))

if __name__ == '__main__':
    main()