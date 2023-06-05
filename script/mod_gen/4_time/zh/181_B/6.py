def solve(n, arr):
    sum = 0
    for i in range(n):
        sum += arr[i][1] - arr[i][0] + 1
    return sum

if __name__ == '__main__':
    solve()