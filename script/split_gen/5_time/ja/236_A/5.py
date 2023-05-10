def swap(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
s = input()
a, b = map(int, input().split())
print(swap(s, a, b))
