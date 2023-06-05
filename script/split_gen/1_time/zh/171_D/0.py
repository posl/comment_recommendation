def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = []
    for i in range(Q):
        BC.append(list(map(int, input().split())))
    #print(N, A, Q, BC)
    sum_A = sum(A)
    #print(sum_A)
    for i in range(Q):
        sum_A += (BC[i][1] - BC[i][0]) * A.count(BC[i][0])
        print(sum_A)
        A = [BC[i][1] if x == BC[i][0] else x for x in A]
        #print(A)
    return
