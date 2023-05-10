def check(x):
    s = str(x)
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) > 1:
            return False
    return True
K = int(input())
cnt = 0
i = 0
while True:
    i += 1
    if check(i):
        cnt += 1
        if cnt == K:
            print(i)
            break
