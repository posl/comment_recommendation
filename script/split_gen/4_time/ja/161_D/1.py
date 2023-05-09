def is_lunlun(n):
    s = str(n)
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) > 1:
            return False
    return True
k = int(input())
lunlun = [i for i in range(1, 10)]
while len(lunlun) < k:
    n = lunlun.pop(0)
    if n % 10 > 0:
        lunlun.append(n*10 + n%10 - 1)
    lunlun.append(n*10 + n%10)
    if n % 10 < 9:
        lunlun.append(n*10 + n%10 + 1)
print(lunlun[0])
