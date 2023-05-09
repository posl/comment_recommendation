def main():
    n = int(input())
    p = list(map(lambda x: int(x) - 1, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == i:
            ans += 1
            if i < n - 1:
                p[i + 1] = i + 1
            else:
                p[0] = 0
    print(ans)
