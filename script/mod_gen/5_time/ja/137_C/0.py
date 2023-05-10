def main():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    s.sort()
    ans = 0
    tmp = 1
    for i in range(N-1):
        if s[i] == s[i+1]:
            tmp += 1
        else:
            ans += tmp*(tmp-1)//2
            tmp = 1
    ans += tmp*(tmp-1)//2
    print(ans)
main()

if __name__ == '__main__':
    main()