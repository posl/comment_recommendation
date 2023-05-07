def main():
    S = input()
    T = "atcoder"
    ans = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()