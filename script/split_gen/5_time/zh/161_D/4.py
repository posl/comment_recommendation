def isRepdigit(n):
    s = str(n)
    for i in range(1,len(s)):
        if abs(int(s[i])-int(s[i-1]))>1:
            return False
    return True
K = int(input())
cnt = 0
for i in range(1,10000000000):
    if isRepdigit(i):
        cnt += 1
    if cnt == K:
        print(i)
        break
