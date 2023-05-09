def main():
    S = input()
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    A = S.count("A")
    B = S.count("B")
    C = S.count("C")
    for t, k in query:
        t %= (A + B + C)
        if t == 0:
            print(S[k - 1])
            continue
        for i in range(t):
            if S[k - 1] == "A":
                k += B
            elif S[k - 1] == "B":
                k += C
            else:
                k -= C
        print(S[k - 1])

if __name__ == '__main__':
    main()