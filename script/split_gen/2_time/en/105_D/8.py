def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M)
    #print(A)
    #print(sum(A))
    #print(sum(A) % M)
    
    mod = [0] * M
    mod[0] = 1
    
    cnt = 0
    sm = 0
    for i in range(N):
        sm += A[i]
        mod[sm % M] += 1
    
    for m in mod:
        cnt += m * (m - 1) // 2
    
    print(cnt)
