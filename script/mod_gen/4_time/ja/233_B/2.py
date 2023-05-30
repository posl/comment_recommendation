def reverse_string(s, l, r):
    return s[:l-1] + s[l-1:r][::-1] + s[r:]
l, r = map(int, input().split())
s = input()
print(reverse_string(s, l, r))
