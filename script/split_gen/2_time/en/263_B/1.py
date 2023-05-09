def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n-1, 0, -1):
        ans += 1
        if p[i-1] == 1:
            break
        else:
            i = p[i-1]
    print(ans)
