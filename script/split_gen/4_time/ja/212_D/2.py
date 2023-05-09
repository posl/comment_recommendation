def main():
    Q = int(input())
    que = []
    for i in range(Q):
        que.append(list(map(int,input().split())))
    bag = []
    for i in range(Q):
        if que[i][0] == 1:
            bag.append(que[i][1])
        elif que[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += que[i][1]
        else:
            print(min(bag))
            bag.remove(min(bag))
