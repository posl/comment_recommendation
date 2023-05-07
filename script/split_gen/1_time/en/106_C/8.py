def findChar(s, k):
    if k <= len(s):
        return s[k - 1]
    else:
        k -= len(s)
        for i in range(9, 1, -1):
            if k <= i * len(s):
                return s[(k - 1) // i]
            else:
                k -= i * len(s)
s = input()
k = int(input())
print(findChar(s, k))
