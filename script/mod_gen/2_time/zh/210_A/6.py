def main():
    N, Q = map(int, input().split())
    #print(N, Q)
    towns = []
    roads = []
    for i in range(N-1):
        a, b = map(int, input().split())
        #print(a, b)
        towns.append([a, b])
    for i in range(Q):
        c, d = map(int, input().split())
        #print(c, d)
        roads.append([c, d])
    for i in range(Q):
        c = roads[i][0]
        d = roads[i][1]
        #print(c, d)
        if c == d:
            print("Town")
            continue
        #print(c, d)
        if c > d:
            c, d = d, c
        #print(c, d)
        for j in range(N-1):
            if towns[j][0] == c and towns[j][1] == d:
                print("Town")
                break
            if towns[j][0] == c and towns[j][1] > d:
                print("Town")
                break
            if towns[j][0] > c and towns[j][1] == d:
                print("Town")
                break
            if towns[j][0] > c and towns[j][1] < d:
                print("Road")
                break
        else:
            print("Road")
    return 0

if __name__ == '__main__':
    main()