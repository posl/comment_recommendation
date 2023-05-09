def solve():
    n = int(input())
    s = input()
    ans = []
    left = 0
    right = n
    for i in range(n):
        if s[i] == "L":
            ans.append(right)
            right -= 1
        else:
            ans.append(left)
            left += 1
    print(*ans[::-1])
solve()
