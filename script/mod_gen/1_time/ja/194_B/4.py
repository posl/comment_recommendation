def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 10**5
    for i in range(N):
        for j in range(N):
            ans = min(ans, max(A[i], B[j]))
    print(ans)

if __name__ == '__main__':
    main()