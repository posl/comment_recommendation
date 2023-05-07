def sum_abs_diffs(arr):
    arr.sort()
    n = len(arr)
    sum = 0
    for i in range(n):
        sum += arr[i] * (2*i - n + 1)
    return sum
n = int(input())
arr = list(map(int, input().split()))
print(sum_abs_diffs(arr))

if __name__ == '__main__':
    sum_abs_diffs()