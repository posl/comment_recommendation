def solve(n, k, arr):
    arr.sort()
    for i in range(n):
        if k >= arr[i][0]:
            k += arr[i][1]
        else:
            return k
    return k + arr[n-1][1]

if __name__ == '__main__':
    solve()