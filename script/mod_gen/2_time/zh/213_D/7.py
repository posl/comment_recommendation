def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    AB.sort(key=lambda x:x[1])
    AB.sort(key=lambda x:x[0])
    print(AB)
    #for i in range(N-1):
    #    if AB[i][0] == 1:
    #        print(AB[i][0], AB[i][1], end=' ')
    #    else:
    #        print(AB[i][1], end=' ')
    #if AB[N-2][1] != 1:
    #    print(1)

if __name__ == '__main__':
    main()