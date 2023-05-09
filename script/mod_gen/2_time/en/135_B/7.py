def main():
    #Write code here
    N = int(input())
    p = list(map(int, input().split()))
    if p == sorted(p):
        print('YES')
    elif p == sorted(p, reverse=True):
        print('NO')
    else:
        if p[0] == 1:
            if p[1] == 2:
                print('YES')
            else:
                print('NO')
        elif p[-1] == N:
            if p[-2] == N-1:
                print('YES')
            else:
                print('NO')
        else:
            p1 = p[:]
            p1[p1.index(1)] = p1[p1.index(1)-1]
            p1[p1.index(1)-1] = 1
            if p1 == sorted(p1):
                print('YES')
            else:
                print('NO')

if __name__ == '__main__':
    main()