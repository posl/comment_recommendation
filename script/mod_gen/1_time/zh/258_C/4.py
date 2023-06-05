def main():
    N, Q = map(int, input().split())
    S = input()
    query = [input().split() for _ in range(Q)]
    for t, x in query:
        if t == '1':
            S = S[-int(x):] + S[:-int(x)]
        else:
            print(S[int(x) - 1])

if __name__ == '__main__':
    main()