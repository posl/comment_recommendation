def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if a[i] < l:
            b[i] = l
        elif a[i] > r:
            b[i] = r
        else:
            b[i] = a[i]
    print(sum(b))
main()
