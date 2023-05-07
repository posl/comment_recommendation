def main():
    S = input()
    K = int(input())
    ans = ""
    for i in range(len(S)):
        if S[i] == "1":
            ans += "1"
        else:
            ans += "1" * (int(S[i]) - 1)
        if len(ans) >= K:
            break
    print(ans[K - 1])
main()

if __name__ == '__main__':
    main()