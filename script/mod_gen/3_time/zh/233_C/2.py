def main():
    N,X = map(int,input().split())
    bag = []
    for i in range(N):
        bag.append(list(map(int,input().split()))[1:])
    #print(bag)
    #print(N,X)
    cnt = 0
    for i in range(N):
        for j in range(len(bag[i])):
            if X%bag[i][j] == 0:
                tmp = X//bag[i][j]
                for k in range(N):
                    if tmp in bag[k]:
                        cnt += 1
    print(cnt)
main()
