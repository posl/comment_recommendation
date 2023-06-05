def find_last(s, c):
    index = -1
    for i in range(len(s)):
        if s[i] == c:
            index = i + 1
    return index
s = input()
c = 'a'
print(find_last(s, c))
