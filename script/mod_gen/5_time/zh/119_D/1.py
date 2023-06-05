def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
    return left
a, b, q = map(int, input().split())
s = [0] * a
t = [0] * b
x = [0] * q
for i in range(a):
    s[i] = int(input())
for i in range(b):
    t[i] = int(input())
for i in range(q):
    x[i] = int(input())
for i in range(q):
    s_index = binary_search(s, x[i])
    t_index = binary_search(t, x[i])
    min_distance = 10 ** 10
    for j in range(2):
        for k in range(2):
            distance = abs(s[s_index - j] - t[t_index - k]) + min(abs(x[i] - s[s_index - j]), abs(x[i] - t[t_index - k]))
            if distance < min_distance:
                min_distance = distance
    print(min_distance)

if __name__ == '__main__':
    binary_search()