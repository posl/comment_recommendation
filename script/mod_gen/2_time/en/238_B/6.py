def findMaxAngle(N, A):
    angles = []
    for i in range(N):
        angles.append(sum(A[:i+1])%360)
    angles.sort()
    maxAngle = 0
    for i in range(N):
        maxAngle = max(maxAngle, angles[i-1]-angles[i])
    return 360-maxAngle

if __name__ == '__main__':
    findMaxAngle()