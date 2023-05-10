def median(array):
    if len(array) % 2 == 0:
        return (array[len(array) // 2 - 1] + array[len(array) // 2]) // 2
    else:
        return array[len(array) // 2]
N = int(input())
A = list(map(int, input().split()))
B = [0]
for i in range(N):
    B.append(B[i] + A[i])
ans = []
for i in range(1, N + 1):
    for j in range(1, N - i + 1):
        ans.append(median(B[j:j + i]))
print(median(ans))

if __name__ == '__main__':
    median()