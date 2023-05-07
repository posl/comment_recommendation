def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    #print(N)
    #print(A)
    #print(Q)
    #print(BC)
    sum_A = sum(A)
    #print(sum_A)
    for i in range(Q):
        B = BC[i][0]
        C = BC[i][1]
        #print(B)
        #print(C)
        #print(A)
        #print(sum_A)
        sum_A = sum_A - B * A.count(B) + C * A.count(B)
        print(sum_A)
        A = [C if a == B else a for a in A]
        #print(A)
