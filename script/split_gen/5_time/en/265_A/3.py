def main():
    x, y, n = map(int, input().split())
    cost = 0
    for i in range(1, n+1):
        if i % 3 == 0:
            cost += y
        else:
            cost += x
    print(cost)
