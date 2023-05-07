def main():
    N = int(input())
    T = list(map(int,input().split()))
    T.sort()
    if N == 1:
        print(T[0])
    else:
        oven1 = T[0]
        oven2 = T[1]
        for i in range(2,N):
            if oven1 < oven2:
                oven1 += T[i]
            else:
                oven2 += T[i]
        print(max(oven1,oven2))

if __name__ == '__main__':
    main()