def main():
    N, Q = map(int, input().split())
    # 0: car number, 1: left, 2: right
    cars = [[i, None, None] for i in range(N+1)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            # connect y to x
            x = query[1]
            y = query[2]
            # find the rightmost car of x
            while cars[x][2]:
                x = cars[x][2]
            # find the leftmost car of y
            while cars[y][1]:
                y = cars[y][1]
            cars[x][2] = y
            cars[y][1] = x
        elif query[0] == 2:
            # disconnect y from x
            x = query[1]
            y = query[2]
            # find the rightmost car of x
            while cars[x][2]:
                x = cars[x][2]
            # find the leftmost car of y
            while cars[y][1]:
                y = cars[y][1]
            cars[x][2] = None
            cars[y][1] = None
        else:
            # print the car numbers of the connected component containing x
            x = query[1]
            # find the leftmost car of x
            while cars[x][1]:
                x = cars[x][1]
            # print the car numbers of the connected component
            ans = []
            while x:
                ans.append(x)
                x = cars[x][2]
            print(len(ans), ' '.join(map(str, ans)))

if __name__ == '__main__':
    main()