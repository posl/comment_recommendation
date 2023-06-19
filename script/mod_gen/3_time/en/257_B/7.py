def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    for i in range(q):
        if l[i] == 1:
            a.sort()
        else:
            a.sort(reverse=True)
        if a[0] == l[i]:
            a[0] = a[1]
        else:
            a[0] = l[i]
    for i in range(k):
        if a[0] == a[i]:
            print(a[0])
        else:
            print(a[1])
main()
