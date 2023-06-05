def count_bottoms(s):
    if s == 'v':
        return 1
    elif s == 'w':
        return 2
    else:
        return 0
s = input()
bottoms = 0
for i in range(len(s)):
    bottoms += count_bottoms(s[i])
print(bottoms)
