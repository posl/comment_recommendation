def main():
    N, Q = map(int, input().split())
    S = input()
    for i in range(Q):
        t, x = map(str, input().split())
        if t == '2':
            print(S[int(x) - 1])
        else:
            S = S[-1] + S[:-1]
    return 0

if __name__ == '__main__':
    main()