def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    ab = [0] * m
    for i in range(m):
        ab[i] = list(map(int, input().split()))
    ab.sort(key=lambda x: x[0])
    ab.sort(key=lambda x: x[1])
    ab.sort(key=lambda x: x[0])
    ab.sort(key=lambda x: x[1])
    print(h)
    print(ab)
    for i in range(m):
        if h[ab[i][0]-1] > h[ab[i][1]-1]:
            h[ab[i][0]-1] = 0
        elif h[ab[i][0]-1] < h[ab[i][1]-1]:
            h[ab[i][1]-1] = 0
        else:
            h[ab[i][0]-1] = 0
            h[ab[i][1]-1] = 0
    print(h)
    print(h.count(0))

if __name__ == '__main__':
    main()