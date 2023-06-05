def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        cnt = 0
        x = i + 1
        while x != -1:
            x = p[x - 1]
            cnt += 1
        ans = max(ans, cnt)
    print(ans)
