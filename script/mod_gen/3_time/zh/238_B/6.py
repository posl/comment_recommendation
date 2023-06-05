def calMaxAngle(N, A):
    maxAngle = 0
    for i in range(N):
        angle = 0
        for j in range(N):
            if i == j:
                continue
            if A[i] > A[j]:
                angle += (A[i] - A[j])
            else:
                angle += (360 - A[j] + A[i])
        if maxAngle < angle:
            maxAngle = angle
    return maxAngle

if __name__ == '__main__':
    calMaxAngle()