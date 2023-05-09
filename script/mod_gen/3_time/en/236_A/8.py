def swap_char (s, a, b):
    s = list(s)
    s[a], s[b] = s[b], s[a]
    return ''.join(s)
s = input()
a, b = map(int, input().split())
print(swap_char(s, a-1, b-1))

if __name__ == '__main__':
    swap_char()