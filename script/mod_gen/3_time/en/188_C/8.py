def main():
    #input
    n = int(input())
    a = list(map(int, input().split()))
    #compute
    for i in range(n):
        b = []
        for j in range(0, 2**(n-i)-1, 2):
            if a[j] > a[j+1]:
                b.append(a[j])
            else:
                b.append(a[j+1])
        a = b
    #output
    print(a[0])

if __name__ == '__main__':
    main()