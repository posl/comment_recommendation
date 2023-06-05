def count_chars(s):
    chars = {}
    for c in s:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars
n = int(input())
strings = []
for i in range(n):
    strings.append(input())
strings_chars = []
for s in strings:
    strings_chars.append(count_chars(s))
count = 0
for i in range(n):
    for j in range(i+1, n):
        if strings_chars[i] == strings_chars[j]:
            count += 1
print(count)
