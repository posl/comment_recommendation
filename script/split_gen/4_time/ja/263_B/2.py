def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += 1
        if p[i] == n:
            break
        else:
            n = p[i]
    print(ans)
