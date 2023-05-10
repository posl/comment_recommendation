def main():
    #input
    n = int(input())
    q = []
    for i in range(n):
        q.append(list(map(int, input().split())))
    
    #process
    a = []
    for i in range(n):
        if q[i][0] == 1:
            a.append(q[i][1])
        elif q[i][0] == 2:
            if len(a) < q[i][2]:
                print(-1)
            else:
                tmp = [x for x in a if x <= q[i][1]]
                tmp.sort(reverse=True)
                print(tmp[q[i][2]-1])
        elif q[i][0] == 3:
            if len(a) < q[i][2]:
                print(-1)
            else:
                tmp = [x for x in a if x >= q[i][1]]
                tmp.sort()
                print(tmp[q[i][2]-1])

if __name__ == '__main__':
    main()