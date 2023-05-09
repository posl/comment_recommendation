def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    max_angle = 0
    for i in range(n):
        angle = 0
        for j in range(n):
            angle += a_list[(i+j)%n]
            max_angle = max(max_angle, angle)
    print(360-max_angle)

if __name__ == '__main__':
    main()