def get_min_spells(N, x, y):
    min_spells = 0
    distances = []
    for i in range(N):
        for j in range(i+1, N):
            distances.append((i,j,abs(x[i]-x[j]),abs(y[i]-y[j])))
    distances.sort(key=lambda x: x[2])
    for i in range(len(distances)):
        for j in range(len(distances)):
            if i == j:
                continue
            if distances[i][0] == distances[j][0] or distances[i][0] == distances[j][1] or distances[i][1] == distances[j][0] or distances[i][1] == distances[j][1]:
                continue
            if distances[i][2] == distances[j][2] and distances[i][3] == distances[j][3]:
                min_spells += 1
                break
    return min_spells

if __name__ == '__main__':
    get_min_spells()