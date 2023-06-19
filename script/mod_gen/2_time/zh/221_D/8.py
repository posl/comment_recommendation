def main():
    n = int(input())
    l = []
    for i in range(n):
        a,b = map(int,input().split())
        l.append([a,b])
    l.sort()
    print(l)
    l2 = []
    for i in range(n):
        l2.append(l[i][0])
        l2.append(l[i][0]+l[i][1])
    print(l2)
    l3 = [0]*(max(l2)+1)
    print(l3)
    for i in l2:
        l3[i] += 1
    print(l3)
    l4 = [0]*(n+1)
    for i in l3:
        l4[i] += 1
    print(l4)
    for i in range(1,n+1):
        print(l4[i],end=" ")
    print()

if __name__ == '__main__':
    main()