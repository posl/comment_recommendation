def main():
    # Get input here
    n, d = map(int, input().split())
    coordinates = []
    for _ in range(n):
        coordinates.append(list(map(int, input().split())))
    # Calculate result here
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            distance = 0
            for k in range(d):
                distance += (coordinates[i][k] - coordinates[j][k]) ** 2
            if (distance ** 0.5).is_integer():
                result += 1
    # Print result here
    print(result)
