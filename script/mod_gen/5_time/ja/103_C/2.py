def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    #print(a)
    f = 0
    for i in range(n):
        f += a[i] * (n - i - 1)
        #print(f)
    print(f)
main()
