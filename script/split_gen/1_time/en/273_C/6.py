def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    K = 0
    ans = [0] * N
    for i in range(N):
        if A[i] != A[i+1]:
            ans[K] += 1
            K = 0
        else:
            K += 1
    print(*ans, sep='\n')
