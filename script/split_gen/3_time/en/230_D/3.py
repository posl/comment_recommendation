def main():
    N, D = [int(x) for x in input().split()]
    walls = []
    for i in range(N):
        L, R = [int(x) for x in input().split()]
        walls.append([L, R])
    walls.sort()
    #print(walls)
    punches = 0
    i = 0
    while i < N:
        j = i
        while j < N and walls[j][0] <= walls[i][0] + D - 1:
            j += 1
        punches += 1
        i = j
    print(punches)
