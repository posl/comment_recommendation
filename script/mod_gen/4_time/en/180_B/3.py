def main():
    import sys
    import math
    # input
    N = int(input())
    x = list(map(int, input().split()))
    # compute
    ans = 0
    for i in range(N):
        ans += abs(x[i])
    print(ans)
    ans = 0
    for i in range(N):
        ans += x[i]**2
    ans = math.sqrt(ans)
    print(ans)
    ans = 0
    for i in range(N):
        if ans < abs(x[i]):
            ans = abs(x[i])
    print(ans)

if __name__ == '__main__':
    main()