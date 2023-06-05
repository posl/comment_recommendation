def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    t = 0
    for i in range(N):
        t += A[i]
    ans = t
    for i in range(N):
        t = t - A[i] + B[i]
        if t > ans:
            ans = t
    print(ans)

if __name__ == '__main__':
    main()