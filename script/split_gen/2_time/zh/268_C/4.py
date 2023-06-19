def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i]] = i
    ans = 0
    c = 0
    for i in range(n):
        if q[i] > c:
            c = q[i]
        else:
            ans += 1
    print(ans)
