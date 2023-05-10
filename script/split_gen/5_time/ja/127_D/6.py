def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]
    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        b, c = bc[j]
        if a[i] < c:
            a[i] = c
            b -= 1
            if b == 0:
                j += 1
        else:
            i += 1
    print(sum(a))
