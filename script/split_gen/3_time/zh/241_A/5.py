def main():
    import sys
    a = [int(x) for x in sys.stdin.readline().strip().split()]
    b = [0] * 10
    for i in range(10):
        b[a[i]] = i
    p = 0
    for i in range(3):
        p = b[p]
    print(p)
main()
