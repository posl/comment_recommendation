def main():
    n = int(input())
    s = input()
    ans = [0] * (n+1)
    left = 0
    right = n
    for i in range(n):
        if s[i] == 'L':
            ans[right] = i+1
            right -= 1
        else:
            ans[left] = i+1
            left += 1
    print(*ans)
