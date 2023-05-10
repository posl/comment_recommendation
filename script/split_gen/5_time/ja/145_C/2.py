def main():
    N = int(input())
    towns = [list(map(int, input().split())) for _ in range(N)]
    #print(towns)
    def calc_distance(a, b):
        return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)
    def calc_path_distance(towns, path):
        distance = 0
        for i in range(N-1):
            distance += calc_distance(towns[path[i]], towns[path[i+1]])
        return distance
    def calc_average_distance(towns):
        path = list(range(N))
        total_distance = 0
        for i in range(N):
            for j in range(N):
                path[i], path[j] = path[j], path[i]
                total_distance += calc_path_distance(towns, path)
                path[i], path[j] = path[j], path[i]
        return total_distance / (N * (N-1))
    print(calc_average_distance(towns))
