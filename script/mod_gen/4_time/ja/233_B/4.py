def reverse_str(s, l, r):
    if l == 1:
        return s[r-1::-1] + s[r:]
    else:
        return s[:l-1] + s[r-1:l-2:-1] + s[r:]
l, r = map(int, input().split())
s = input()
print(reverse_str(s, l, r))

if __name__ == '__main__':
    reverse_str()