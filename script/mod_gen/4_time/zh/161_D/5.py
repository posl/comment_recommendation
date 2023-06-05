def isLuckyNumber(x):
    if x < 10:
        return True
    else:
        x = str(x)
        for i in range(0, len(x)-1):
            if abs(int(x[i])-int(x[i+1])) > 1:
                return False
        return True
K = int(input())
count = 0
i = 0
while count < K:
    i += 1
    if isLuckyNumber(i):
        count += 1
print(i)

if __name__ == '__main__':
    isLuckyNumber()