def main():
    n,m = map(int,input().split())
    k = []
    s = []
    p = []
    for i in range(m):
        k.append(list(map(int,input().split()))[0])
        s.append(list(map(int,input().split())))
    p = list(map(int,input().split()))
    ans = 0
    for i in range(2**n):
        flag = True
        for j in range(m):
            on = 0
            for sij in s[j]:
                if (i >> (sij-1)) & 1:
                    on += 1
            if on % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()