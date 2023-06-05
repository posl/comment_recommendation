def main():
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        a.append(list(map(int,input().split())))
    min_a = a[0][0]
    for i in range(h):
        for j in range(w):
            if min_a > a[i][j]:
                min_a = a[i][j]
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a
    print(ans)
