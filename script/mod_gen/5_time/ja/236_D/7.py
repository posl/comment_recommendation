def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    #print(a)
    max = 0
    for i in range(2**n):
        #print(i)
        tmp = 0
        for j in range(n):
            for k in range(j+1, n):
                #print(j, k)
                if ((i >> j) & 1) == ((i >> k) & 1):
                    tmp += a[j][k]
        if tmp > max:
            max = tmp
    print(max)

if __name__ == '__main__':
    main()