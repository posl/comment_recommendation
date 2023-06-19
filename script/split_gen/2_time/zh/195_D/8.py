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
        l = query[i][0]
        r = query[i][1]
        x_copy = x.copy()
        x_copy.pop(l-1)
        x_copy.pop(r-2)
        x_copy.sort(reverse=True)
        wv_copy = wv.copy()
        wv_copy.sort(key=lambda x:x[1],reverse=True)
        #print(wv_copy)
        #print(x_copy)
        for j in range(len(x_copy)):
            for k in range(len(wv_copy)):
                if wv_copy[k][0] <= x_copy[j]:
                    wv_copy.pop(k)
                    break
        #print(wv_copy)
        sum = 0
        for j in range(len(wv_copy)):
            sum += wv_copy[j][1]
        print(sum)
