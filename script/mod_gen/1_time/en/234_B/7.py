def main():
    N = int(input())
    points = [[int(x) for x in input().split()] for _ in range(N)]
    max_length = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                length = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
                if length > max_length:
                    max_length = length
    print(max_length)

if __name__ == '__main__':
    main()