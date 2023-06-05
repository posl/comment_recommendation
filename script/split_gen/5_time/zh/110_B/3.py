def main():
    n, m, x, y = map(int, input().split())
    xList = list(map(int, input().split()))
    yList = list(map(int, input().split()))
    z = 0
    for i in range(x + 1, y + 1):
        if max(xList) < i and min(yList) >= i:
            z = i
            break
    if z == 0:
        print("战争")
    else:
        print("无战争")
