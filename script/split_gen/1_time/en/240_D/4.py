def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = {}
    for i in a:
        cnt[i] = cnt.get(i, 0) + 1
    ans = 0
    for k, v in cnt.items():
        ans = max(ans, v)
    print(ans)
