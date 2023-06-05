def main():
    n, q = map(int, input().split())
    #print(n, q)
    a = list(map(int, input().split()))
    #print(a)
    k = []
    for i in range(q):
        k.append(int(input()))
    #print(k)
    a.sort()
    #print(a)
    #print(k)
    #print(len(a))
    #print(len(k))
    for i in range(q):
        #print(k[i])
        #print(len(a))
        #print(a[len(a) - 1])
        if k[i] > a[len(a) - 1]:
            print(k[i] + len(a))
        else:
            for j in range(len(a)):
                if k[i] <= a[j]:
                    print(k[i] + j)
                    break
    return

if __name__ == '__main__':
    main()