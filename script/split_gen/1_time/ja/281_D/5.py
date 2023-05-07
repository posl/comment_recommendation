def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    #print(A)
    #print(A[0:K])
    print(sum(A[0:K])//D)
