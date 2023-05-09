def main():
    #read input
    n,k = map(int,input().split())
    td = [list(map(int,input().split())) for i in range(n)]
    #sort by deliciousness
    td.sort(key=lambda x:x[1],reverse=True)
    #use set to count variety
    kind = set()
    #use heap to store the "deliciousness" of pieces you eat
    h = []
    #base total deliciousness
    total = 0
    for i in range(k):
        total += td[i][1]
        kind.add(td[i][0])
        heapq.heappush(h,td[i][1])
    #calculate satisfaction
    ans = total + len(kind)*len(kind)
    for i in range(k,n):
        #if the kind of topping is new
        if td[i][0] not in kind:
            #update total deliciousness
            total += td[i][1] - heapq.heappop(h)
            #update variety
            kind.add(td[i][0])
            #update satisfaction
            ans = max(ans,total+len(kind)*len(kind))
    print(ans)
