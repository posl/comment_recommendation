def last_index(s):
    for i in range(len(s)):
        if s[i] == 'a':
            index = i+1
    return index
s = input()
print(last_index(s))
