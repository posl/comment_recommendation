def main():
    from collections import Counter
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [0]*Q
    C = [0]*Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())
    Ac = Counter(A)
    ans = sum(A)
    for i in range(Q):
        ans += (C[i] - B[i])*Ac[B[i]]
        Ac[C[i]] += Ac[B[i]]
        Ac[B[i]] = 0
        print(ans)

if __name__ == '__main__':
    main()