def is_lunlun(n):
    s = str(n)
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) > 1:
            return False
    return True
k = int(input())
lunlun = []
for i in range(1,10):
    lunlun.append(i)
while len(lunlun) < k:
    n = lunlun.pop(0)
    for i in range(max(0,n%10-1),min(10,n%10+2)):
        lunlun.append(n*10+i)
print(lunlun[0])

if __name__ == '__main__':
    is_lunlun()