def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort(reverse=True)
    B.sort(reverse=True)
    ans = 0
    for i in range(N):
        if A[i] > B[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()