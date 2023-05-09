def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    cnt = 1
    for i in range(n):
        d += l[i]
        if d <= x:
            cnt += 1
        else:
            break
    print(cnt)
