def main():
    N = int(input())
    towns = []
    for i in range(N):
        towns.append(list(map(int, input().split())))
    #print(towns)
    import itertools
    all_routes = list(itertools.permutations(range(N), N))
    #print(all_routes)
    sum = 0
    for route in all_routes:
        for i in range(N-1):
            sum += ((towns[route[i]][0] - towns[route[i+1]][0])**2 + (towns[route[i]][1] - towns[route[i+1]][1])**2)**0.5
    print(sum/len(all_routes))
