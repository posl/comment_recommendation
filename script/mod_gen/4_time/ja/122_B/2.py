def main():
    s = input()
    ans = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] in 'ACGT':
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()