def problem171_d():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    BC = [list(map(int,input().split())) for _ in range(Q)]
    
    sum_A = sum(A)
    count = {}
    for i in A:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    for i in range(Q):
        sum_A -= count[BC[i][0]] * BC[i][0]
        sum_A += count[BC[i][0]] * BC[i][1]
        if BC[i][1] in count:
            count[BC[i][1]] += count[BC[i][0]]
        else:
            count[BC[i][1]] = count[BC[i][0]]
        count[BC[i][0]] = 0
        print(sum_A)

if __name__ == '__main__':
    problem171_d()