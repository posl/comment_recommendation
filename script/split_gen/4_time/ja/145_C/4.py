def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)
import itertools
n = int(input())
towns = []
for _ in range(n):
    x, y = map(int, input().split())
    towns.append((x,y))
routes = list(itertools.permutations(towns))
sum = 0
for route in routes:
    for i in range(len(route)-1):
        sum += distance(route[i][0], route[i][1], route[i+1][0], route[i+1][1])
print(sum/len(routes))
