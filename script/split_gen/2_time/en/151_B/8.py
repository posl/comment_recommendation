def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, M)
    #print(A)
    score = sum(A)
    #print(score)
    required = M*N
    #print(required)
    if required - score <= K:
        if required - score < 0:
            print(0)
        else:
            print(required - score)
    else:
        print(-1)
