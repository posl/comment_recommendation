def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        X, Y = map(int, input().split())
        if (X**2 + Y**2)**(1/2) <= D:
            count += 1
    print(count)
