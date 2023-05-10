def main():
    N = int(input())
    XY = []
    for i in range(N):
        x, y = map(int, input().split())
        XY.append((x, y))
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def get_ab(x1, y1, x2, y2):
        a = x2 - x1
        b = y2 - y1
        g = gcd(a, b)
        a //= g
        b //= g
        return (a, b)
    ab = set()
    for i in range(N):
        for j in range(i + 1, N):
            ab.add(get_ab(XY[i][0], XY[i][1], XY[j][0], XY[j][1]))
    print(len(ab) + 1)
