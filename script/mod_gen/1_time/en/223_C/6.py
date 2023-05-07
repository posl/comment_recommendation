def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    res = 0
    for i in range(N):
        res += A[i]/B[i]
    res = res*2/N
    print(res)

if __name__ == '__main__':
    main()