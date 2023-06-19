def main():
    N, X = map(int, input().split())
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = ""
    for i in range(N):
        ans += s[(X - 1) % 26]
        X = (X - 1) // 26
    print(ans[::-1])
main()
