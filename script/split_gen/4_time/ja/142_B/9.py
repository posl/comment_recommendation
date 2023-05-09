def main():
    n,k = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for height in h:
        if height >= k:
            ans += 1
    print(ans)
