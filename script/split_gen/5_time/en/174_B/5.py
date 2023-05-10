def main():
    n, d = map(int, input().split())
    count = 0
    for i in range(n):
        x, y = map(int, input().split())
        dist = (x**2+y**2)**(1/2)
        if dist <= d:
            count += 1
    print(count)
