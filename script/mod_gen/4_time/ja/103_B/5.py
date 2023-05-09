def rotate(s, n):
    return s[n:] + s[:n]
s = input()
t = input()
for i in range(len(s)):
    if rotate(s, i) == t:
        print('Yes')
        exit()
print('No')

if __name__ == '__main__':
    rotate()