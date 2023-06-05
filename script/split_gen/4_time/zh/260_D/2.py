def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    q = [0] * n
    r = [0] * n
    for i in range(n):
        q[p[i]-1] = i
    for i in range(n):
        if i < k:
            r[i] = i
        else:
            r[i] = max(r[i-k], q[i])
    for i in range(n):
        if r[i] == n-1:
            print(-1)
        else:
            print(r[i]+2)
