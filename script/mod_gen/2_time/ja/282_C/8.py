def main():
    N = int(input())
    S = input()
    ans = ""
    flag = 0
    for i in range(N):
        if S[i] == '"':
            flag += 1
        elif S[i] == ',' and flag % 2 == 1:
            ans += S[i]
        else:
            ans += "."
    print(ans)

if __name__ == '__main__':
    main()