def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(x-1, 0)
    a = list(map(lambda x: x-1, a))
    cnt = 1
    i = x-1
    while True:
        i = a[i]
        if i == 0:
            break
        cnt += 1
    print(cnt)
