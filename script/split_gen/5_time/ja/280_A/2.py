def main():
    H,W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        ans += S[i].count("#")
    print(ans)
