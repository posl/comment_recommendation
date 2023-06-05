def main():
    n,m = map(int,input().split())
    s_c = []
    for i in range(m):
        s_c.append(list(map(int,input().split())))
    s_c.sort()
    num = 0
    for i in range(m):
        num += s_c[i][1] * 10 ** (n - s_c[i][0])
    if len(str(num)) == n:
        print(num)
    else:
        print(-1)
