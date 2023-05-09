def main():
    n = int(input())
    data = []
    for i in range(n):
        x, y = map(int, input().split())
        data.append([x, y])
    import itertools
    import math
    sum = 0
    for i in itertools.permutations(data):
        for j in range(n-1):
            sum += math.sqrt((i[j][0]-i[j+1][0])**2 + (i[j][1]-i[j+1][1])**2)
    print(sum/math.factorial(n))
