def main():
    import heapq
    q = int(input())
    que = []
    for i in range(q):
        que.append(list(map(int,input().split())))
    #print(que)
    num = 0
    for i in range(q):
        if que[i][0] == 1:
            heapq.heappush(que[i],que[i][1]-num)
        elif que[i][0] == 2:
            num += que[i][1]
        else:
            print(heapq.heappop(que[i])+num)
            que[i] = []

if __name__ == '__main__':
    main()