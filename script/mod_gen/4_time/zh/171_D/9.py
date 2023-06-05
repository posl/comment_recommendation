def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    sumA = sum(A)
    dic = {}
    for i in range(N):
        if A[i] not in dic:
            dic[A[i]] = 1
        else:
            dic[A[i]] += 1
    for i in range(Q):
        sumA += (BC[i][1] - BC[i][0]) * dic.get(BC[i][0], 0)
        if BC[i][1] in dic:
            dic[BC[i][1]] += dic.get(BC[i][0], 0)
            dic[BC[i][0]] = 0
        else:
            dic[BC[i][1]] = dic.get(BC[i][0], 0)
            dic[BC[i][0]] = 0
        print(sumA)

if __name__ == '__main__':
    main()