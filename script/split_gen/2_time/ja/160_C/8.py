def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    #A.append(K + A[0])
    #print(A)
    #print(len(A))
    ans = 0
    for i in range(len(A) - 1):
        ans += min(A[i+1] - A[i], K - A[i+1] + A[i])
    print(ans)
