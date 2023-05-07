def main():
    n,d = map(int,input().split())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort(key = lambda x:x[1])
    cnt = 0
    for i in range(n):
        if l[i][0] > l[i][1]:
            continue
        for j in range(i+1,n):
            if l[i][1]+d-1 < l[j][0]:
                break
            if l[i][1]+d-1 >= l[j][1]:
                l[j][0] = l[i][1]+d
            else:
                l[j][0] = l[i][1]+d
                cnt += 1
                break
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()