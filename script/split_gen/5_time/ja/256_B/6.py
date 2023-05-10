def main():
    n = int(input())
    a = list(map(int,input().split()))
    p = 0
    for i in range(n):
        p += a[i]
        if p >= 4:
            p -= 4
    print(p)
main()
