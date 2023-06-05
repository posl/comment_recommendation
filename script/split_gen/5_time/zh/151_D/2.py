def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for si in S:
        ans += si.count('.')
    if ans == H + W - 1:
        ans -= 1
    print(ans)
