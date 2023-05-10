def main():
    x, y, n = map(int, input().split())
    cost = 10000000000
    for i in range(n+1):
        for j in range(n+1):
            if i + j == n:
                cost = min(cost, i*x + j*y)
    print(cost)
