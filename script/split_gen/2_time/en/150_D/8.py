def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    ans = 0
    for i in range(1, M+1):
        for j in range(N):
            if i % A[j] == 0:
                ans += 1
                break
    print(ans)