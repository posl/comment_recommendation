def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0]*m
    for i in range(n):
        b[a[i]%m] += 1
    ans = 0
    for i in range(m):
        if b[i] == 0:
            continue
        for j in range(i+1, m):
            if b[j] == 0:
                continue
            if (i+j)%m == 0:
                if b[i] < b[j]:
                    ans += b[i]
                else:
                    ans += b[j]
                b[i] = 0
                b[j] = 0
                break
        if (i+i)%m == 0:
            ans += b[i]//2
            b[i] = b[i]%2
    for i in range(m):
        if b[i] == 0:
            continue
        if i == 0 or i*2 == m:
            ans += b[i]//2
        else:
            ans += b[i]
    print(ans)
