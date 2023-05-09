def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort(reverse=True)
    b.sort(reverse=True)
    #print(a)
    #print(b)
    a_count = 0
    b_count = 0
    for i in range(n):
        #print(a_count, b_count)
        if a_count > b_count:
            b_count += b[i]
        else:
            a_count += a[i]
        #print(a_count, b_count)
    if a_count > b_count:
        print(n)
    else:
        print(n-1)

if __name__ == '__main__':
    main()