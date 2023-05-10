def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    max_angle = 0
    for i in range(N):
        angle = A[i]
        for j in range(i+1, N):
            angle += A[j]
            if angle >= 360:
                angle = angle % 360
        if max_angle < angle:
            max_angle = angle
        #print(i, angle)
    print(360 - max_angle)
