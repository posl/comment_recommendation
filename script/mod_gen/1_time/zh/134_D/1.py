def main():
    N = int(input())
    a = list(map(int,input().split()))
    b = [0]*N
    c = [0]*N
    for i in range(N):
        if a[i] == 1:
            if i+1 > N//2:
                b[i] = 1
            else:
                c[i] = 1
    if sum(b) == 0:
        print(0)
    elif sum(b) > sum(c):
        print(sum(b))
        for i in range(N):
            if b[i] == 1:
                print(i+1,end=' ')
        print('')
    else:
        print(sum(c))
        for i in range(N):
            if c[i] == 1:
                print(i+1,end=' ')
        print('')

if __name__ == '__main__':
    main()