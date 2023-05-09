def main():
    N = int(input())
    S = input()
    ans = ""
    cnt = 0
    for i in range(N):
        if S[i] == '"':
            cnt += 1
            if cnt % 2 == 0:
                ans += '"'
            else:
                ans += '"'
        elif S[i] == ',':
            if cnt % 2 == 0:
                ans += ','
            else:
                ans += '.'
        else:
            ans += S[i]
    print(ans)

if __name__ == '__main__':
    main()