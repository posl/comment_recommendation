def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1
s = int(input())
a = [s]
i = 1
while True:
    a.append(f(a[i-1]))
    if a[i] in a[:i]:
        print(i+1)
        break
    else:
        i += 1

if __name__ == '__main__':
    f()