def main():
    n, k = map(int, input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    #print(d)
    #print(a)
    ans = 0
    for i in range(n):
        if i+1 not in a[0]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()