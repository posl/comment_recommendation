def main():
    S = input()
    ans = 0
    pre = S[0]
    for i in range(1, len(S)):
        if S[i] == pre:
            ans += 1
        pre = S[i]
    print(ans)

if __name__ == '__main__':
    main()