def main():
    # get the number of people and the number of people who will receive lights of the same strength
    n, k = map(int, input().split())
    # get the people who will receive lights of the same strength
    a = list(map(int, input().split()))
    # get the coordinates of the people
    xy = [list(map(int, input().split())) for _ in range(n)]
    # get the maximum distance between any two people
    # first, get the distance between any two people
    d = []
    for i in range(n):
        for j in range(i+1, n):
            d.append(((xy[i][0] - xy[j][0])**2 + (xy[i][1] - xy[j][1])**2)**0.5)
    # then, get the maximum distance between any two people
    r = max(d)
    # then, calculate the minimum strength of the lights needed for every person to be lit by at least one light
    # first, sort the people who will receive lights of the same strength
    a.sort()
    # then, calculate the minimum strength of the lights needed for every person to be lit by at least one light
    for i in range(k):
        r = max(r, d[a[i]-1])
    # then, print the minimum strength of the lights needed for every person to be lit by at least one light
    print(r)

if __name__ == '__main__':
    main()