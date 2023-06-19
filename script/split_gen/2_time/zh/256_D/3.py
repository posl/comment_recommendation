def main():
    n = int(input())
    lr = []
    for i in range(n):
        lr.append(list(map(int, input().split())))
    lr.sort()
    minL = lr[0][0]
    maxR = lr[0][1]
    for i in range(1, n):
        if lr[i][0] <= maxR:
            maxR = max(maxR, lr[i][1])
        else:
            print(minL, maxR)
            minL = lr[i][0]
            maxR = lr[i][1]
    print(minL, maxR)
