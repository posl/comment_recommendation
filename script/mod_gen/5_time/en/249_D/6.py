def solve():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if A[i] * A[j] == A[k]:
                    count += 1
    print(count)

if __name__ == '__main__':
    solve()