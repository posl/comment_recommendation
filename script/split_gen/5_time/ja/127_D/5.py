def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    bc = [list(map(int, input().split())) for _ in range(m)]
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if bc[j][0] > 0:
            a[i] = bc[j][1]
            bc[j][0] -= 1
            i += 1
        else:
            j += 1
    print(sum(a))
