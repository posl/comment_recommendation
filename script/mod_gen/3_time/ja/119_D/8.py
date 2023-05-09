def find_nearest(arr, num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return arr[mid]
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return arr[right]
A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
x = [int(input()) for _ in range(Q)]
for i in range(Q):
    ans = 10 ** 20
    near_s = find_nearest(s, x[i])
    near_t = find_nearest(t, x[i])
    ans = min(ans, abs(near_s - x[i]) + abs(near_t - near_s))
    ans = min(ans, abs(near_t - x[i]) + abs(near_s - near_t))
    print(ans)

if __name__ == '__main__':
    find_nearest()