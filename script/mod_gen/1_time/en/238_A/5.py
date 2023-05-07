def f(n):
    if 2**n > n**2:
        print("Yes")
    else:
        print("No")
n = int(input())
f(n)

if __name__ == '__main__':
    f()