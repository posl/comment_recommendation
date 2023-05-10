def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    diff = []
    for i in range(m-1):
        diff.append(x[i+1]-x[i])
    diff.sort()
    ans = 0
    for i in range(m-n):
        ans += diff[i]
    print(ans)
