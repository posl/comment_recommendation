def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    #print(a)
    m = a[0] - 1
    #print(m)
    cnt = 0
    while True:
        #print(m)
        for i in range(n):
            cnt += m % a[i]
        if cnt > m:
            break
        else:
            cnt = 0
            m += 1
    print(m)

if __name__ == '__main__':
    main()