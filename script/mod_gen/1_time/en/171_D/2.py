def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    ans = sum(A)
    for i in range(Q):
        ans += (C[i] - B[i]) * A.count(B[i])
        print(ans)

if __name__ == '__main__':
    main()