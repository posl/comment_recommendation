def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    #print(a.index(min(a)))
    #print(b[a.index(min(a))])
    #print(min(a))
    #print(b[a.index(min(a))])
    if m <= b[a.index(min(a))]:
        print(min(a) * m)
    else:
        print(min(a) * b[a.index(min(a))] + min(a) * (m - b[a.index(min(a))]))

if __name__ == '__main__':
    main()