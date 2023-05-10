def solve():
    # Implement solution here
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n-k):
        if a[i] >= a[i+k]:
            return 'Yes'
    return 'No'
result = solve()
print(result)
