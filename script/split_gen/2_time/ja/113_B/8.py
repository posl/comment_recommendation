def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    #print(N, T, A, H)
    temp = 10000000000
    ans = 0
    for i in range(N):
        if temp > abs(A - (T - H[i]*0.006)):
            temp = abs(A - (T - H[i]*0.006))
            ans = i + 1
    print(ans)
