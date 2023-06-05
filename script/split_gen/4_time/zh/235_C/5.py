def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        x_i, k_i = map(int, input().split())
        cnt = 0
        for j in range(N):
            if A[j] == x_i:
                cnt += 1
            if cnt == k_i:
                print(j+1)
                break
        else:
            print(-1)
