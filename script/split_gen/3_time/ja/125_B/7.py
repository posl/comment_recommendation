def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    # print(n, v, c)
    ans = 0
    for i in range(n):
        if v[i] - c[i] > 0:
            ans += v[i] - c[i]
    print(ans)
