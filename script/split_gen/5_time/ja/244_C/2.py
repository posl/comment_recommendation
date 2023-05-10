def main():
    n = int(input())
    a = [0]*(2*n+2)
    a[1] = 1
    a[2*n+1] = 1
    print(1)
    x = int(input())
    if x == 0:
        return
    if x == 2*n+1:
        print(2*n)
        return
    a[x] = 1
    print(2*n+1)
    y = int(input())
    if y == 0:
        return
    if a[y] == 0:
        print(y)
        return
    else:
        print(2*n)
        return
