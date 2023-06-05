def f(x):
    s = 0
    for i in range(1, x+1):
        if x % i == 0:
            s += 1
    return s
n = int(input())
s = 0
for i in range(1, n+1):
    s += i * f(i)
print(s)

if __name__ == '__main__':
    f()