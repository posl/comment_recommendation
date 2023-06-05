def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1
s=int(input())
a=[s]
while True:
    s=f(s)
    if s in a:
        print(len(a)+1)
        break
    else:
        a.append(s)

if __name__ == '__main__':
    f()