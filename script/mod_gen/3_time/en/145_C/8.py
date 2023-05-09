def main():
    from itertools import permutations
    import math
    N = int(input())
    town = [list(map(int,input().split())) for _ in range(N)]
    path = list(permutations(range(N)))
    ans = 0
    for i in range(len(path)):
        for j in range(N-1):
            ans += math.sqrt((town[path[i][j]][0]-town[path[i][j+1]][0])**2+(town[path[i][j]][1]-town[path[i][j+1]][1])**2)
    print(ans/len(path))

if __name__ == '__main__':
    main()