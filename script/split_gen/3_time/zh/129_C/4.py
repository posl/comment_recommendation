def main():
    N, M = input().split()
    N = int(N)
    M = int(M)
    A = []
    for i in range(M):
        A.append(int(input()))
    A.sort()
    A.append(N)
    A.insert(0, 0)
    ans = 1
    for i in range(M+1):
        ans *= pow(2, A[i+1]-A[i]-1, 1000000007)
        ans %= 1000000007
    print(ans)
