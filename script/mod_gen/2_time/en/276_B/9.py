def main():
    # get input
    n, m = map(int, input().split())
    # create a list of lists
    # the i-th list contains the cities directly connected to city i
    road = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        road[a-1].append(b-1)
        road[b-1].append(a-1)
    # sort the lists in ascending order
    for i in range(n):
        road[i].sort()
    # print the results
    for i in range(n):
        print(len(road[i]), end=' ')
        for j in range(len(road[i])):
            print(road[i][j]+1, end=' ')
        print()

if __name__ == '__main__':
    main()