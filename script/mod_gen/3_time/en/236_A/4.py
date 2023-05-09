def swap(s, a, b):
    a = a - 1
    b = b - 1
    s = s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]
    return s
s = input()
a, b = map(int, input().split())
print(swap(s, a, b))

if __name__ == '__main__':
    swap()