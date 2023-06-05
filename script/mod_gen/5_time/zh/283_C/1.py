def main():
    S = input()
    l = len(S)
    ans = 100000
    for i in range(l-1):
        if S[i] == '0':
            continue
        else:
            ans = min(ans, i+l-1-i+int(S[i:]))
    print(ans)

if __name__ == '__main__':
    main()