def main():
    n,m,q = map(int,input().split())
    wv = []
    for i in range(n):
        wv.append(list(map(int,input().split())))
    x = list(map(int,input().split()))
    query = []
    for i in range(q):
        query.append(list(map(int,input().split())))
    for i in range(q):
        l,r = query[i]
        box = x[:l-1]+x[r:]
        box.sort()
        box = box[::-1]
        wv.sort(key=lambda x:x[1],reverse=True)
        ans = 0
        for i in range(n):
            for j in range(len(box)):
                if box[j] >= wv[i][0]:
                    ans += wv[i][1]
                    box.pop(j)
                    break
        print(ans)

if __name__ == '__main__':
    main()