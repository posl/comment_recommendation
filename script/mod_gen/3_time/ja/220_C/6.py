def main():
    N = int(input())
    A = list(map(int,input().split()))
    X = int(input())
    B = A * 1000000
    S = 0
    for i in range(1000000*N):
        S += B[i]
        if S > X:
            print(i+1)
            break

if __name__ == '__main__':
    main()