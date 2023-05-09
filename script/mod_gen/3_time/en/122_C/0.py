def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * Q
    r = [0] * Q
    for i in range(Q):
        l[i], r[i] = map(int, input().split())
        l[i] -= 1
        r[i] -= 1
    #print(N, Q)
    #print(S)
    #print(l)
    #print(r)
    #ACの出現回数を求める
    AC = [0] * N
    for i in range(1, N):
        if S[i - 1] == "A" and S[i] == "C":
            AC[i] = AC[i - 1] + 1
        else:
            AC[i] = AC[i - 1]
    #print(AC)
    #クエリごとにACの出現回数を求める
    for i in range(Q):
        print(AC[r[i]] - AC[l[i]])

if __name__ == '__main__':
    main()