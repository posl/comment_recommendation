def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(N)]
    #print(N, K, A, XY)
    min_x = min([x for x, y in XY])
    max_x = max([x for x, y in XY])
    min_y = min([y for x, y in XY])
    max_y = max([y for x, y in XY])
    #print(min_x, max_x, min_y, max_y)
    min_r = 10**10
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            r = max([((x - x0)**2 + (y - y0)**2)**0.5 for x0, y0 in XY])
            #print(x, y, r)
            if r < min_r:
                min_r = r
    print(min_r)
main()
