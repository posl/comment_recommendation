def main():
    N = int(input())
    S = input()
    ans = ""
    flag = False
    for s in S:
        if s == '"':
            flag = not flag
        elif s == ',' and not flag:
            ans += '.'
        else:
            ans += s
    print(ans)

if __name__ == '__main__':
    main()