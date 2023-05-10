def count(s, i):
    l = 0
    while i + l < len(s):
        if s[l] != s[i + l]:
            l += 1
        else:
            break
    return l
n = int(input())
s = input()
for i in range(1, n):
    print(count(s, i))

if __name__ == '__main__':
    count()