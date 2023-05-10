def isSGS(n):
    s = str(n)
    return s.count('7') > 0 and s.count('5') > 0 and s.count('3') > 0
n = int(input())
cnt = 0
for i in range(1, n + 1):
    if isSGS(i):
        cnt += 1
print(cnt)

if __name__ == '__main__':
    isSGS()