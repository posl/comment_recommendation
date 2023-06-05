def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
dict = {}
for i in range(n):
    for j in range(n):
        if i != j:
            x1 = x[j] - x[i]
            y1 = y[j] - y[i]
            if x1 < 0:
                x1 = -x1
                y1 = -y1
            if x1 == 0:
                y1 = 1
            elif y1 == 0:
                x1 = 1
            else:
                g = gcd(x1, y1)
                x1 //= g
                y1 //= g
            if (x1, y1) not in dict:
                dict[(x1, y1)] = 1
            else:
                dict[(x1, y1)] += 1

if __name__ == '__main__':
    gcd()