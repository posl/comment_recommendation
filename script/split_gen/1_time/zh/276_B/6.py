def main():
    n,m = map(int,input().split())
    road = []
    for i in range(m):
        road.append(list(map(int,input().split())))
    road.sort()
    for i in range(1,n+1):
        print(len([j for j in road if j[0] == i or j[1] == i]),end = ' ')
        for j in road:
            if j[0] == i and j[1] != i:
                print(j[1],end = ' ')
            elif j[1] == i and j[0] != i:
                print(j[0],end = ' ')
        print()
main()
