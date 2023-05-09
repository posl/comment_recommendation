def main():
    p = list(map(int, input().split()))
    s = [chr(97 + i) for i in range(26)]
    ans = [0] * 26
    for i in range(26):
        ans[p[i] - 1] = s[i]
    print(''.join(ans))

if __name__ == '__main__':
    main()