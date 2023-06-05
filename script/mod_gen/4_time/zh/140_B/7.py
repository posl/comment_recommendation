def main():
    #读取数据
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    #计算满意度积分
    score = 0
    score += B[A[0]-1]
    for i in range(1, N):
        score += B[A[i]-1]
        if A[i] == A[i-1] + 1:
            score += C[A[i-1]-1]
    print(score)

if __name__ == '__main__':
    main()