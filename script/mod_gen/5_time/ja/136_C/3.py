def solve():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(1, N):
        if H[i-1] > H[i]:
            H[i] += 1
    for i in range(1, N):
        if H[i-1] > H[i]:
            print('No')
            break
    else:
        print('Yes')

if __name__ == '__main__':
    solve()