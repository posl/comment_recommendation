def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    bonus = []
    for _ in range(m):
        bonus.append(list(map(int,input().split())))
    now = 0
    for i in range(n):
        now += a[i]
        if now > t:
            print('No')
            return
        for j in range(m):
            if i+1 == bonus[j][0]:
                now += bonus[j][1]
                if now > t:
                    print('No')
                    return
    print('Yes')
    return

if __name__ == '__main__':
    main()