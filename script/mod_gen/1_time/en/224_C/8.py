def main():
    # Get input
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    # Count the number of triangles
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if is_triangle(XY[i], XY[j], XY[k]):
                    count += 1
    # Output
    print(count)

if __name__ == '__main__':
    main()