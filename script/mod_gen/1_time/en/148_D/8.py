def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(a)
    #print(n)
    #print(a)
    #print(sorted(a))
    #print(sorted(a) == list(range(1, n+1)))
    if sorted(a) == list(range(1, n+1)):
        print(0)
        return
    if a[0] != 1:
        print(-1)
        return
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = i
    #print(b)
    max = 0
    for i in range(n):
        if b[i] > max:
            max = b[i]
        if max < i:
            print(-1)
            return
    print(n - max - 1)
main()

if __name__ == '__main__':
    main()