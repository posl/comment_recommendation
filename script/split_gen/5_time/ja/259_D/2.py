def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    xyr = [list(map(int, input().split())) for _ in range(N)]
    xyr = [[x, y, r] for x, y, r in xyr]
    #print(xyr)
    def is_reachable(xyr):
        def is_in_circle(x, y, r):
            #print(x, y, r)
            return (x - s_x) ** 2 + (y - s_y) ** 2 <= r ** 2 and (x - t_x) ** 2 + (y - t_y) ** 2 <= r ** 2
        for x, y, r in xyr:
            if is_in_circle(x, y, r):
                return True
        return False
    print("Yes" if is_reachable(xyr) else "No")
main()
