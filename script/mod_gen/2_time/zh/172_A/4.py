def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    BC = [list(map(int,input().split())) for _ in range(Q)]
    sum_A = sum(A)
    BC = sorted(BC,key = lambda x:x[1],reverse = True)
    for i in range(Q):
        sum_A = sum_A - A[BC[i][0]-1] * (BC[i][1]-BC[i][0])
        A[BC[i][0]-1] = BC[i][1]
        print(sum_A)

if __name__ == '__main__':
    main()