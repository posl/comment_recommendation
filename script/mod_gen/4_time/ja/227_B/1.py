def solve():
    N = int(input())
    S = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for a in range(1, 1000):
                for b in range(1, 1000):
                    if S[i] == 4 * a * b + 3 * a + 3 * b:
                        if S[j] == 4 * a * b + 3 * a + 3 * b:
                            count += 1
    print(N - count // 2)

if __name__ == '__main__':
    solve()