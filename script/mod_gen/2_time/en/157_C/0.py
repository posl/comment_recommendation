def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    for i in range(1000):
        s = str(i)
        if len(s) != N:
            continue
        ok = True
        for j in range(M):
            if s[S[j] - 1] != str(C[j]):
                ok = False
                break
        if ok:
            print(s)
            return
    print(-1)
main()

if __name__ == '__main__':
    main()