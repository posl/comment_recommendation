def get_max_angle(A):
    N = len(A)
    max_angle = 0
    for i in range(N):
        angle = A[i]
        if angle > max_angle:
            max_angle = angle
    return max_angle
