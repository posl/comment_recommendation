def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1])
    #print(AB)
    #print(AB[0][1])
    for i in range(N-1):
        if AB[i][1] < AB[i+1][0]:
            print(AB[i][1])
            exit()
    print(AB[-1][1])

if __name__ == '__main__':
    main()