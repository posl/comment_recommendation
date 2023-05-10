def solve():
    N = int(input())
    H = list(map(int, input().split()))
    for i in reversed(range(1, N)):
        if H[i-1] > H[i]:
            H[i-1] -= 1
    for i in range(N-1):
        if H[i] > H[i+1]:
            print('No')
            return
    print('Yes')
