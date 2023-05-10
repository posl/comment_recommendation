def check(n):
    if n < 10:
        return True
    else:
        s = str(n)
        for i in range(1, len(s)):
            if abs(int(s[i]) - int(s[i-1])) > 1:
                return False
    return True
k = int(input())
cnt = 0
n = 1
while True:
    if check(n):
        cnt += 1
        if cnt == k:
            print(n)
            break
    n += 1
