def main():
    N = int(input())
    cities = []
    for i in range(N):
        cities.append(list(map(int, input().split())))
    #print(cities)
    import itertools
    import math
    sum = 0
    count = 0
    for i in itertools.permutations(cities, N):
        #print(i)
        for j in range(N-1):
            sum += math.sqrt((i[j][0]-i[j+1][0])**2+(i[j][1]-i[j+1][1])**2)
        count += 1
    print(sum/count)
main()
