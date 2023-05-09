def main():
    N, K, D = list(map(int, input().split()))
    A = list(map(int, input().split()))
    
    S = set()
    for i in range(K):
        S |= set([sum(A[j:j+i+1]) for j in range(N-i)])
    S = sorted(list(S), reverse=True)
    for s in S:
        if s % D == 0:
            print(s)
            return
    print(-1)
main()
I think this is a good problem to learn about the set data type. I think it is very useful to know about it. I also think that this problem is a good problem to learn about the sorted function. I think it is very useful to know about it.
