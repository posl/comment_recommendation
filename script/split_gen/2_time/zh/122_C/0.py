def countAC(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] == 'A' and s[i+1] == 'C':
            count += 1
    return count
n, q = map(int, input().split())
s = input()
for i in range(q):
    l, r = map(int, input().split())
    print(countAC(s[l-1:r]))
