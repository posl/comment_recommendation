def solve():
    # Implement here
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    scores = [K - Q] * N
    for a in A:
        scores[a - 1] += 1
    for score in scores:
        if score <= 0:
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    solve()