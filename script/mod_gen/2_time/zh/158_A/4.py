def main():
    n,m,k = map(int,input().split())
    l = []
    for i in range(m):
        l.append(list(map(int,input().split())))
    l2 = []
    for i in range(k):
        l2.append(list(map(int,input().split())))
    l3 = []
    for i in range(n):
        l3.append(0)
    for i in range(m):
        l3[l[i][0]-1] += 1
        l3[l[i][1]-1] += 1
    for i in range(k):
        l3[l2[i][0]-1] -= 1
        l3[l2[i][1]-1] -= 1
    for i in range(n):
        l3[i] -= 1
    for i in range(n):
        print(l3[i],end=" ")

if __name__ == '__main__':
    main()