def lunlun(n):
    if n < 10:
        return [n]
    else:
        a = []
        for i in range(1, 10):
            a.extend(lunlun(i*10+n%10-1))
            a.extend(lunlun(i*10+n%10))
            a.extend(lunlun(i*10+n%10+1))
        return a
n = int(input())
a = []
for i in range(1, 10):
    a.extend(lunlun(i))
a.sort()
print(a[n-1])

if __name__ == '__main__':
    lunlun()