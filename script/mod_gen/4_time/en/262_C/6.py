def solve():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if A[i] == i + 1:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    solve()