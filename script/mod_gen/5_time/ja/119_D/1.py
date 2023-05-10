def get_nearest(arr, num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if num == arr[mid]:
            return num
        elif num < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if right < 0:
        return arr[left]
    elif left > len(arr) - 1:
        return arr[right]
    if abs(num - arr[left]) < abs(num - arr[right]):
        return arr[left]
    else:
        return arr[right]
A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]
X = [int(input()) for _ in range(Q)]
for x in X:
    s = get_nearest(S, x)
    t = get_nearest(T, x)
    ans = min(abs(x - s), abs(x - t))
    ans = min(ans, abs(s - t) + min(abs(s - x), abs(t - x)))
    print(ans)

if __name__ == '__main__':
    get_nearest()