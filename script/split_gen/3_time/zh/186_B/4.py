def main():
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        a.append(list(map(int,input().split())))
    min_num = min(min(a))
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_num
    print(ans)
