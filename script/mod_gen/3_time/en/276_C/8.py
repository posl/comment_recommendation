def get_permutation(n, k):
    ans = []
    for i in range(1, n+1):
        ans.append(i)
    for i in range(k-1):
        for j in range(n-1, 0, -1):
            if ans[j-1] < ans[j]:
                break
        for k in range(n-1, j-1, -1):
            if ans[j-1] < ans[k]:
                break
        ans[j-1], ans[k] = ans[k], ans[j-1]
        ans[j:] = ans[j:][::-1]
    return ans
n = int(input())
p = list(map(int, input().split()))
k = 1
for i in range(n):
    k += (p[i] - 1) * math.factorial(n - i - 1)
print(*get_permutation(n, k))

if __name__ == '__main__':
    get_permutation()