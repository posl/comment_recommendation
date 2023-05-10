def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    A.append(A[0])
    max_angle = 0
    for i in range(N):
        angle = A[i] - A[i+1]
        if angle < 0:
            angle += 360
        if angle > max_angle:
            max_angle = angle
    print(max_angle)

if __name__ == '__main__':
    main()