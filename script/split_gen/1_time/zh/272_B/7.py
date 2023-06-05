def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for i in range(M)]
    ans = 'Yes'
    for i in range(N):
        for j in range(i+1, N):
            for k in range(M):
                if i+1 not in A[k] or j+1 not in A[k]:
                    ans = 'No'
                    break
    print(ans)
