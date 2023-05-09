def main():
    import math
    import itertools
    N = int(input())
    city = []
    for i in range(N):
        x, y = map(int, input().split())
        city.append([x, y])
    distance = []
    for i in range(N):
        for j in range(N):
            distance.append(math.sqrt((city[i][0]-city[j][0])**2+(city[i][1]-city[j][1])**2))
    permutation = list(itertools.permutations(distance, N))
    sum = 0
    for i in range(len(permutation)):
        sum += sum(permutation[i])
    print(sum/len(permutation))
main()
