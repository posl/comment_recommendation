def is_rurun(x):
    if x < 10:
        return True
    s = str(x)
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) > 1:
            return False
    return True
k = int(input())
cnt = 0
i = 1
while True:
    if is_rurun(i):
        cnt += 1
        if cnt == k:
            print(i)
            break
    i += 1
