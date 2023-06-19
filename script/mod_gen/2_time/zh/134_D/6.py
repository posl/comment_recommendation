def solve():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N, 0, -1):
        if sum(b[i-1::i]) % 2 != a[i-1]:
            b[i-1] = 1
    M = sum(b)
    print(M)
    if M != 0:
        print(' '.join(map(str, [i+1 for i in range(N) if b[i]])))

if __name__ == '__main__':
    solve()