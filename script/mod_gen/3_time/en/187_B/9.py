def solve(n, points):
    result = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]) <= 1:
                result += 1
    return result

if __name__ == '__main__':
    solve()