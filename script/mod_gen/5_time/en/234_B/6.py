def main():
    import math
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    
    max_len = 0
    for i in range(N):
        for j in range(i+1, N):
            length = math.sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
            if length > max_len:
                max_len = length
    print(max_len)

if __name__ == '__main__':
    main()