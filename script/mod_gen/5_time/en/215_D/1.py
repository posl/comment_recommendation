def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = list(set(a))
b = []
for i in range(1, m + 1):
    if i not in a:
        b.append(i)
c = []
for i in b:
    flag = True
    for j in a:
        if gcd(i, j) == 1:
            pass
        else:
            flag = False
            break
    if flag:
        c.append(i)
print(len(c))
for i in c:
    print(i)

if __name__ == '__main__':
    gcd()