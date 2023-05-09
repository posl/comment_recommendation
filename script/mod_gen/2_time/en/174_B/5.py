def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        x, y = map(int, input().split())
        dist = (x**2 + y**2)**0.5
        if dist <= D:
            count += 1
    print(count)

if __name__ == '__main__':
    main()