def run():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = []
    for _ in range(q):
        l.append(int(input()))
    s = [0] * n
    for i in range(k):
        s[a[i]-1] += 1
    for i in range(n):
        if s[i] > 0:
            if s[i] - q <= 0:
                print("Yes")
            else:
                print("No")
