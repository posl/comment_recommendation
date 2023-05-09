def main():
    # input
    N = int(input())
    T = list(map(int, input().split()))
    # compute
    ans = 0
    for i in range(N):
        ans += T[i]
    ans = ans - max(T) + max(T)/2
    # output
    print(int(ans))
