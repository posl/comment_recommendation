def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    if M == 0:
        print(1)
        return
    
    A.sort()
    A.append(N + 1)
    B = [A[0] - 1]
    for i in range(M):
        B.append(A[i + 1] - A[i] - 1)
    B.sort(reverse = True)
    
    ans = 0
    for i in range(M):
        if B[i] > 0:
            ans += B[i]
    
    print(ans + 1)
