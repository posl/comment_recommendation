def check(x):
    s = str(x)
    for i in range(1,len(s)):
        if abs(int(s[i-1])-int(s[i])) > 1:
            return False
    return True
K = int(input())
cnt = 0
x = 0
while cnt < K:
    x += 1
    if check(x):
        cnt += 1
print(x)
