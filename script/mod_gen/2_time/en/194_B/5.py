def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = float('inf')
    for i in range(N):
        for j in range(N):
            ans = min(ans, max(A[i], B[j]) if i != j else A[i] + B[j])
    print(ans)

if __name__ == '__main__':
    main()