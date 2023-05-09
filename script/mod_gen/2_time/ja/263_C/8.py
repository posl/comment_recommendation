def rec(arr, n, m):
    if len(arr) == n:
        print(*arr)
        return
    for i in range(1, m+1):
        if len(arr) == 0:
            rec(arr+[i], n, m)
        elif arr[-1] < i:
            rec(arr+[i], n, m)
n, m = list(map(int, input().split()))
rec([], n, m)

if __name__ == '__main__':
    rec()