def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min_p = p[0]
    for i in range(n):
        if min_p >= p[i]:
            ans += 1
            min_p = p[i]
    print(ans)
