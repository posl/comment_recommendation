def main():
    n,w = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    #print(a)
    #print(w)
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum > w:
            break
    print(i)

if __name__ == '__main__':
    main()