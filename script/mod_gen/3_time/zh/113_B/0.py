def main():
    N = int(input())
    T,A = map(int,input().split())
    H = list(map(int,input().split()))
    temp = 100000
    index = 0
    for i in range(N):
        if abs(A - (T-H[i]*0.006)) < temp:
            temp = abs(A - (T-H[i]*0.006))
            index = i
    print(index+1)

if __name__ == '__main__':
    main()