def main():
    # Get input here
    N, D = [int(x) for x in input().split()]
    points = [[int(x) for x in input().split()] for i in range(N)]
    # Calculate result here
    result = 0
    for i in range(N):
        for j in range(i+1, N):
            sum = 0
            for k in range(D):
                sum += (points[i][k] - points[j][k]) ** 2
            if sum ** 0.5 == int(sum ** 0.5):
                result += 1
    # Print result here
    print(result)
main()
