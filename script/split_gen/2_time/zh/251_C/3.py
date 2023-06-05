def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    if W <= 10**6:
        ans = 0
        for i in range(1, W+1):
            for j in range(1, W+1):
                for k in range(1, W+1):
                    if i*A[0] + j*A[1] + k*A[2] == W:
                        ans += 1
        print(ans)
