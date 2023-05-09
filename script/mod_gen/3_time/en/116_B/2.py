def f(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1
s = int(input())
a = [s]
for i in range(1,1000000):
    a.append(f(a[i-1]))
    if len(a) != len(set(a)):
        print(i+1)
        break

if __name__ == '__main__':
    f()