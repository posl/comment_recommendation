def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    #print(a)
    h = 0
    for i in range(n):
        if h < a[i]:
            h = a[i]
        else:
            if a[i] > 0:
                h = (a[i] // h + 1) * h
    print(h)
main()
