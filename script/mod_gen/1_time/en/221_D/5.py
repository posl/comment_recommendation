def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int,input().split())
        A.append(a)
        B.append(b)
    ans = [0 for i in range(N+1)]
    for i in range(N):
        ans[A[i]] += 1
        ans[A[i]+B[i]] -= 1
    for i in range(1,N+1):
        ans[i] += ans[i-1]
    for i in range(1,N+1):
        print(ans[i],end=' ')
    print()
    return

if __name__ == '__main__':
    main()