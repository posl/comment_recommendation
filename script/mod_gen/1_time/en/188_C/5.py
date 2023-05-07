def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a = [(x,i) for i,x in enumerate(a)]
    for i in range(n-1):
        b = []
        for j in range(2**(n-i-1)):
            if a[2*j][0] > a[2*j+1][0]:
                b.append(a[2*j])
            else:
                b.append(a[2*j+1])
        a = b
    if a[0][0] > a[1][0]:
        print(a[1][1]+1)
    else:
        print(a[0][1]+1)

if __name__ == '__main__':
    main()