def solve(h, w, A):
    ans = []
    for i in range(h):
        for j in range(w):
            if i%2 == 0:
                if j == w-1:
                    if i == h-1:
                        break
                    else:
                        if A[i+1][j]%2 == 1:
                            ans.append([i+1, j+1, i+2, j+1])
                            A[i+1][j] -= 1
                else:
                    if A[i][j+1]%2 == 1:
                        ans.append([i+1, j+1, i+1, j+2])
                        A[i][j+1] -= 1
            else:
                if j == 0:
                    if A[i+1][j]%2 == 1:
                        ans.append([i+1, j+1, i+2, j+1])
                        A[i+1][j] -= 1
                else:
                    if A[i][j-1]%2 == 1:
                        ans.append([i+1, j+1, i+1, j])
                        A[i][j-1] -= 1
    return ans
h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
ans = solve(h, w, A)
print(len(ans))
for a in ans:
    print(*a)
