def reverse(s, l, r):
    return s[:l] + s[l:r+1][::-1] + s[r+1:]
l, r = map(int, input().split())
s = input()
print(reverse(s, l-1, r-1))
