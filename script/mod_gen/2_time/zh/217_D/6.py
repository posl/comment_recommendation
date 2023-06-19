def main():
    l,q = map(int,input().split())
    mark = [0 for i in range(q)]
    for i in range(q):
        mark[i] = list(map(int,input().split()))
    #print(mark)
    mark.sort(key=lambda x:x[1])
    #print(mark)
    mark.insert(0,[0,0])
    mark.append([0,l])
    #print(mark)
    mark1 = []
    mark2 = []
    for i in range(1,len(mark)-1):
        if mark[i][0] == 1:
            mark1.append(mark[i][1])
        else:
            mark2.append(mark[i][1])
    #print(mark1)
    #print(mark2)
    mark1.sort()
    mark2.sort()
    #print(mark1)
    #print(mark2)
    mark1.insert(0,0)
    mark1.append(l)
    mark2.insert(0,0)
    mark2.append(l)
    #print(mark1)
    #print(mark2)
    for i in range(1,len(mark1)):
        mark1[i] = mark1[i] - mark1[i-1]
    for i in range(1,len(mark2)):
        mark2[i] = mark2[i] - mark2[i-1]
    #print(mark1)
    #print(mark2)
    ans = 0
    for i in mark1:
        for j in mark2:
            if i == j:
                ans = i
                break
    print(ans)

if __name__ == '__main__':
    main()