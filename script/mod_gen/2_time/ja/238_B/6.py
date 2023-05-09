def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [i%360 for i in A]
    max_angle = 0
    for i in range(N):
        angle = 0
        for j in range(N):
            if j <= i:
                angle += A[j]
            else:
                angle -= A[j]
        if angle > max_angle:
            max_angle = angle
    print(max_angle)

if __name__ == '__main__':
    main()