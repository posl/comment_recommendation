def max_without_index(arr, index):
    arr.pop(index)
    return max(arr)
N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
for i in range(N):
    print(max_without_index(A[:], i))
