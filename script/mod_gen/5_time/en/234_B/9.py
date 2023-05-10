def main():
    # Get the number of points
    num_points = int(input())
    # Create a list of points
    points = []
    # Loop through the number of points
    for i in range(num_points):
        # Get the point
        point = input().split()
        # Add the point to the list
        points.append(point)
    # Create a list of distances
    distances = []
    # Loop through the points
    for i in range(num_points):
        # Loop through the points
        for j in range(num_points):
            # Get the distance between the points
            distance = (((int(points[i][0]) - int(points[j][0])) ** 2) + ((int(points[i][1]) - int(points[j][1])) ** 2)) ** 0.5
            # Add the distance to the list
            distances.append(distance)
    # Print the maximum distance
    print(max(distances))
main()

if __name__ == '__main__':
    main()