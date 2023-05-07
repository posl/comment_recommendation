def main():
    S = input()
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    A = S.count("A")
    B = S.count("B")
    C = S.count("C")
    for t, k in query:
        t %= (A + B + C)
        for _ in range(t):
            if S[k - 1] == "A":
                k = (k - 1) % B + A + 1
            elif S[k - 1] == "B":
                k = (k - 1) % C + A + B + 1
            else:
                k = (k - 1) % A + 1
        print(S[k - 1])

if __name__ == '__main__':
    main()