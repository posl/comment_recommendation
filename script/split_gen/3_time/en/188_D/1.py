def main():
    N, C = map(int, input().split())
    A = []
    for i in range(N):
        a, b, c = map(int, input().split())
        A.append([a, c])
        A.append([b+1, -c])
    A.sort()
    ans = 0
    sum = 0
    prev = 0
    for a in A:
        ans += min(C, sum) * (a[0] - prev)
        sum += a[1]
        prev = a[0]
    print(ans)
