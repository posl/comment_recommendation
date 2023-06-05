def maxDistance(points):
    ans = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            ans = max(ans, distance(points[i], points[j]))
    return ans

if __name__ == '__main__':
    maxDistance()