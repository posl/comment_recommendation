def main():
    #read input
    N = int(input())
    black_cells = []
    for i in range(N):
        black_cells.append([int(j) for j in input().split()])
    #find the number of connected components
    #all black cells are connected if and only if
    #the minimum distance between any two black cells is less than or equal to 2.
    #Otherwise, there are two connected components.
    min_distance = 10000
    for i in range(N):
        for j in range(i+1,N):
            distance = max(abs(black_cells[i][0]-black_cells[j][0]),abs(black_cells[i][1]-black_cells[j][1]))
            if distance < min_distance:
                min_distance = distance
    if min_distance <= 2:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()