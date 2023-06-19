def f(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return 3*n+1
s = int(input())
a = [s]
while True:
    next = f(a[-1])
    if next in a:
        print(len(a)+1)
        break
    else:
        a.append(next)

if __name__ == '__main__':
    f()