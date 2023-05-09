def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    diff = [v[i] - c[i] for i in range(n)]
    ans = 0
    for i in range(n):
        if diff[i] > 0:
            ans += diff[i]
    print(ans)
