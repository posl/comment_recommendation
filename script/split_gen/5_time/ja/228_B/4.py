def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i-1 for i in a]
    known = [False] * n
    known[x-1] = True
    cnt = 1
    for i in range(n):
        if known[a[i]]:
            cnt += 1
            known[i] = True
    print(cnt)
