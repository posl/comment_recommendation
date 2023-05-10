def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        ans = max(ans, A[i] + B[i])
    print(ans)
main()

if __name__ == '__main__':
    main()