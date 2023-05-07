def main():
    N = int(input())
    AB = []
    for i in range(N-1):
        AB.append([int(i) for i in input().split()])
    AB.sort()
    #print(AB)
    A = [AB[0][0]]
    B = [AB[0][1]]
    for i in range(1,N-1):
        if AB[i][0] in B:
            A.append(AB[i][0])
            B.append(AB[i][1])
        else:
            A.append(AB[i][1])
            B.append(AB[i][0])
    A.append(AB[N-2][1])
    #print(A)
    print(*A, sep=' ')
main()
