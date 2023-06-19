def solve(s, k):
    n = len(s)
    max_consecutive_x = 0
    consecutive_x = 0
    for i in range(n):
        if s[i] == 'X':
            consecutive_x += 1
        else:
            max_consecutive_x = max(max_consecutive_x, consecutive_x)
            consecutive_x = 0
    max_consecutive_x = max(max_consecutive_x, consecutive_x)
    max_consecutive_x += k
    max_consecutive_x = min(max_consecutive_x, n)
    return max_consecutive_x
s = input()
k = int(input())
print(solve(s, k))
