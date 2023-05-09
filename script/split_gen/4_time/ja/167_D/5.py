def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    v = [0]*n
    v[0] = 1
    next = a[0]-1
    cnt = 1
    while v[next] == 0:
        v[next] = 1
        next = a[next]-1
        cnt += 1
    if k <= cnt:
        for i in range(k):
            next = a[next]-1
        print(next+1)
    else:
        k -= cnt
        k %= cnt
        for i in range(k):
            next = a[next]-1
        print(next+1)
