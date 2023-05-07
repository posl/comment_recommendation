def main():
    N, K = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    #print(A)
    #print(N, K)
    #K回テレポートするまでのループ
    for i in range(K):
        #print(A[i])
        if A[i] == 2:
            print(2)
            break
        else:
            A.append(A[A[i]])
    else:
        #K回テレポートした後のループ
        #print(A)
        #print(K%N)
        print(A[K%N])
