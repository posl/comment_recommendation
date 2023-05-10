def find_distance(n, a):
    distance = [0]*(2*n+1)
    for i in range(n):
        distance[a[i]] = 1
    for i in range(2, 2*n+1):
        distance[i] = distance[i//2] + 1
    return distance

if __name__ == '__main__':
    find_distance()