def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for _ in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    
    S1 = S[:N]
    S2 = S[N:]
    for t, a, b in zip(T, A, B):
        if t == 1:
            if a <= N:
                if b <= N:
                    S1 = S1[:a-1] + S1[b-1] + S1[a:b-1] + S1[a-1] + S1[b:]
                else:
                    S1 = S1[:a-1] + S2[b-N-1] + S1[a:b-N-1] + S1[a-1] + S1[b-N:]
                    S2 = S2[:b-N-1] + S1[a-1] + S2[a:b-N-1] + S2[b-N:]
            else:
                if b <= N:
                    S1 = S1[:b-1] + S2[a-N-1] + S1[b:a-N-1] + S1[b-1] + S1[a-N:]
                    S2 = S2[:a-N-1] + S1[b-1] + S2[b:a-N-1] + S2[a-N:]
                else:
                    S2 = S2[:a-N-1] + S2[b-N-1] + S2[a-N:b-N-1] + S2[a-N-1] + S2[b-N:]
        else:
            S1, S2 = S2, S1
    
    print(S1 + S2)

if __name__ == '__main__':
    main()