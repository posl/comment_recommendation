def f(n):
    if n==0:
        return 1
    else:
        return n*f(n-1)
k = int(input())
n = 1
while True:
    if f(n)%k==0:
        print(n)
        break
    else:
        n+=1

if __name__ == '__main__':
    f()