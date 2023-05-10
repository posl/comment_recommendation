def main():
    n,a,b,c = map(int,input().split())
    l = [int(input()) for i in range(n)]
    ans = 10**9
    for i in range(4**n):
        tmp = [0 for j in range(3)]
        mp = 0
        for j in range(n):
            if i%4 == 0 and tmp[0] > 0:
                mp += 10
            elif i%4 == 1 and tmp[1] > 0:
                mp += 10
            elif i%4 == 2 and tmp[2] > 0:
                mp += 10
            if i%4 == 0:
                tmp[0] += l[j]
            elif i%4 == 1:
                tmp[1] += l[j]
            elif i%4 == 2:
                tmp[2] += l[j]
            i //= 4
        if tmp[0] == 0 or tmp[1] == 0 or tmp[2] == 0:
            continue
        mp += abs(tmp[0]-a) + abs(tmp[1]-b) + abs(tmp[2]-c) - 30
        ans = min(ans,mp)
    print(ans)

if __name__ == '__main__':
    main()