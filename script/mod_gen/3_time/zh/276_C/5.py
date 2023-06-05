def get_next_permutation(arr):
    n = len(arr)
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            break
    else:
        return arr[::-1]
    for j in range(n - 1, i, -1):
        if arr[j] > arr[i]:
            break
    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = arr[i + 1:][::-1]
    return arr
n = int(input())
p = list(map(int, input().split()))
p = get_next_permutation(p)
print(*p)

if __name__ == '__main__':
    get_next_permutation()