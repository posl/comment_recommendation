def isLucky(x):
    s = str(x)
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) > 1:
            return False
    return True
k = int(input())
count = 0
i = 1
while count < k:
    if isLucky(i):
        count += 1
    i += 1
print(i-1)

if __name__ == '__main__':
    isLucky()