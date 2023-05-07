def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = A[::-1]
    A.append(360)
    A.append(0)
    A = A[::-1]
    #print(A)
    max_angle = 0
    for i in range(N+1):
        diff = A[i+1] - A[i]
        if diff < 0:
            diff += 360
        #print(diff)
        max_angle = max(max_angle, diff)
    print(360 - max_angle)

if __name__ == '__main__':
    main()