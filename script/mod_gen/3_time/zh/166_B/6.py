def solve():
    n,k = map(int,input().split())
    a = [0] * n
    for i in range(k):
        d = int(input())
        A = list(map(int,input().split()))
        for j in range(d):
            a[A[j]-1] += 1
    cnt = 0
    for i in range(n):
        if a[i] == 0:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    solve()