def main():
    x, y, n = map(int, input().split())
    min_cost = 1000
    for i in range(1, n+1):
        for j in range(0, n+1):
            if i + 3*j == n:
                cost = x*i + y*j
                if cost < min_cost:
                    min_cost = cost
    print(min_cost)
