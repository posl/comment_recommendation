def swap(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
S = input()
a, b = map(int, input().split())
print(swap(S, a, b))

if __name__ == '__main__':
    swap()