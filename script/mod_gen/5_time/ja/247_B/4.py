def main():
    N = int(input())
    s_t = [input().split() for _ in range(N)]
    s = [s_t[i][0] for i in range(N)]
    t = [s_t[i][1] for i in range(N)]
    ans = 'No'
    for i in range(N):
        if s[i] != t[i]:
            if s[i] in t:
                ans = 'Yes'
                break
    print(ans)

if __name__ == '__main__':
    main()