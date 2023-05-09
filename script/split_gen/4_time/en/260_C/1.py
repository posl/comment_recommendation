def main():
    a = input()
    a = a.split()
    n = int(a[0])
    x = int(a[1])
    y = int(a[2])
    if n == 1:
        print(0)
    else:
        print((n-1)*x+y)
