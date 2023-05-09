def find(s, i):
    l = 0
    while i + l < len(s):
        if s[l] == s[i + l]:
            break
        l += 1
    return l
n = int(input())
s = input()
for i in range(1, n):
    print(find(s, i))

if __name__ == '__main__':
    find()