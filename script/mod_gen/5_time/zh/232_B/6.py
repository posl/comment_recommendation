def move(s, k):
    return chr((ord(s) - ord('a') + k) % 26 + ord('a'))
s = input()
t = input()
for i in range(26):
    for j in range(len(s)):
        if move(s[j], i) != t[j]:
            break
    else:
        print('Yes')
        exit()
print('No')

if __name__ == '__main__':
    move()