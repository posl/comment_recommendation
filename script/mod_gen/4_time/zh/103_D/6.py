def main():
    N,M = map(int,input().split())
    a = []
    b = []
    for i in range(M):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    print(a,b)
    a.sort()
    b.sort()
    print(a,b)
    print(a[-1],b[0])
    if a[-1] <= b[0]:
        print(b[0]-a[-1])
    else:
        print(0)

if __name__ == '__main__':
    main()