def main():
    n = int(input())
    p = [int(x) - 1 for x in input().split()]
    ans = 0
    for i in range(n):
        now = i
        cnt = 0
        while now != -1:
            now = p[now]
            cnt += 1
        ans = max(ans, cnt)
    print(ans)
