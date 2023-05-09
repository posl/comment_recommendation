def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    B = [True]*N
    for i in range(N):
        if B[i]:
            for j in range(i+1,N):
                if A[j]%A[i]==0:
                    B[j] = False
    print(sum(B))
