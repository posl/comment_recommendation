def count_dot(S):
    count = 0
    for i in range(len(S)):
        if S[i] == ".":
            count += 1
    return count
H, W = map(int, input().split())
A = []
for i in range(H):
    A.append(input())
count = 0
for i in range(H):
    count += count_dot(A[i])
print(count)
