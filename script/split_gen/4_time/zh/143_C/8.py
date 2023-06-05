def merge(s):
    if len(s) == 1:
        return 1
    elif len(s) == 2:
        return 2 if s[0] != s[1] else 1
    else:
        return merge(s[:len(s)//2]) + merge(s[len(s)//2:])
n = int(input())
s = input()
print(merge(s))
