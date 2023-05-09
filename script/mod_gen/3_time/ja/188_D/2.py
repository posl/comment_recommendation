def main():
    N, C = map(int, input().split())
    A = []
    for i in range(N):
        a, b, c = map(int, input().split())
        A.append([a, c])
        A.append([b+1, -c])
    A.sort()
    ans = 0
    tmp = 0
    for i in range(len(A)):
        ans += min(C, tmp) * (A[i][0] - A[i-1][0])
        tmp += A[i][1]
    print(ans)

if __name__ == '__main__':
    main()