def reverse_string(s, l, r):
    l -= 1
    r -= 1
    return s[:l] + s[l:r+1][::-1] + s[r+1:]
l, r = map(int, input().split())
s = input()
print(reverse_string(s, l, r))

if __name__ == '__main__':
    reverse_string()