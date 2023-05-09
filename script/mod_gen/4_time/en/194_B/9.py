def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    #print(N)
    #print(AB)
    print(min([max(AB[i][0],AB[i][1]) for i in range(N)]))

if __name__ == '__main__':
    main()