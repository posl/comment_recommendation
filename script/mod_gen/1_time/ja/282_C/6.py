def main():
    N = int(input())
    S = input()
    ans = ""
    flag = False
    for i in range(N):
        if S[i] == '"':
            flag = not flag
        elif S[i] == ',' and flag == False:
            ans += '.'
        else:
            ans += S[i]
    print(ans)

if __name__ == '__main__':
    main()