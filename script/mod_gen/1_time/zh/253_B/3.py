def find_o(s):
    for i in range(len(s)):
        if s[i] == 'o':
            return i
    return -1
h, w = [int(x) for x in input().split()]
s = []
for i in range(h):
    s.append(input())

if __name__ == '__main__':
    find_o()