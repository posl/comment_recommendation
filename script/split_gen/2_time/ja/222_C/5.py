def main():
    N, M = map(int, input().split())
    A = [input() for i in range(2*N)]
    win = [0]*2*N
    next = [i for i in range(2*N)]
    for i in range(M):
        for j in range(N):
            if A[next[2*j]][i] == A[next[2*j+1]][i]:
                pass
            elif A[next[2*j]][i] == 'G' and A[next[2*j+1]][i] == 'C':
                win[next[2*j]] += 1
            elif A[next[2*j]][i] == 'C' and A[next[2*j+1]][i] == 'P':
                win[next[2*j]] += 1
            elif A[next[2*j]][i] == 'P' and A[next[2*j+1]][i] == 'G':
                win[next[2*j]] += 1
            else:
                win[next[2*j+1]] += 1
        next = sorted(next, key=lambda x: (-win[x], x))
        #print(next)
    for i in next:
        print(i+1)
