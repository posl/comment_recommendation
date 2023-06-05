def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = [0]
    for i in range(n):
        d.append(d[i] + l[i])
    cnt = 0
    for i in d:
        if i <= x:
            cnt += 1
    print(cnt)
