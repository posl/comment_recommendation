def main():
    n = int(input())
    l = [i for i in range(1, 2 * n + 2)]
    for i in range(n + 1):
        print(l[i])
        print(l[-(i + 1)])
        a = int(input())
        if a == 0:
            break
        b = int(input())
        if b == 0:
            break
        l.remove(a)
        l.remove(b)
