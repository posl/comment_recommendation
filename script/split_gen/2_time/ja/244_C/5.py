def main():
    n = int(input())
    a = list(range(1, 2*n+2))
    for i in range(n):
        print(a[i])
        b = int(input())
        if b == 0:
            return
        a.remove(b)
    print(a[0])
    return
