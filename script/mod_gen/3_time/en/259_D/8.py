def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    xyr = [list(map(int, input().split())) for _ in range(N)]
    #print(xyr)
    def dist(x1, y1, x2, y2):
        return ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    def is_in_circle(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) <= xyr[2]
    def is_in_circle2(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) < xyr[2]
    def is_on_circle(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) == xyr[2]
    def is_on_circle2(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) == xyr[2] - 10**(-6)
    def is_in_circle3(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) < xyr[2] - 10**(-6)
    def is_on_circle3(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) == xyr[2] - 10**(-6)
    def is_on_circle4(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) == xyr[2] + 10**(-6)
    def is_on_circle5(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) == xyr[2] + 10**(-6)
    def is_on_circle6(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) == xyr[2] - 10**(-6)
    def is_in_circle4(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) < xyr[2] + 10**(-6)
    def is_in_circle5

if __name__ == '__main__':
    main()