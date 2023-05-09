def main():
    S = input()
    K = int(input())
    ans = ""
    for s in S:
        if s == "1":
            ans += "1"
        else:
            ans += "9" * (int(s) - 1)
            ans += "8"
        if len(ans) >= K:
            print(ans[K - 1])
            return

if __name__ == '__main__':
    main()