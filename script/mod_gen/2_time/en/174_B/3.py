def problem174_b():
    n, d = map(int, input().split())
    count = 0
    for _ in range(n):
        x, y = map(int, input().split())
        if (x**2 + y**2)**(1/2) <= d:
            count += 1
    print(count)

if __name__ == '__main__':
    problem174_b()