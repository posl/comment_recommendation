def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [list(map(int, input().split())) for i in range(m)]
    a.sort(reverse=True)
    b.sort(key=lambda x:x[1], reverse=True)
    j = 0
    for i in range(n):
        if j < m and a[i] < b[j][1]:
            a[i] = b[j][1]
            b[j][0] -= 1
            if b[j][0] == 0:
                j += 1
    print(sum(a))
