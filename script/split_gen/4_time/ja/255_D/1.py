def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    for _ in range(q):
        x.append(int(input()))
    for i in range(q):
        cnt = 0
        for j in range(n):
            cnt += abs(a[j] - x[i])
        print(cnt)
    return
