def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_angle = 0
    for i in range(N):
        angle = 0
        for j in range(N):
            angle += A[(j + i) % N]
            max_angle = max(max_angle, min(angle, 360 - angle))
    print(360 - max_angle)

if __name__ == '__main__':
    main()