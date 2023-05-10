def solve():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            elif A[i] % 3 == 0:
                A[i] = A[i] // 3
            else:
                break
        else:
            cnt += 1
            continue
        break
    if all(a == A[0] for a in A):
        print(cnt)
    else:
        print(-1)

if __name__ == '__main__':
    solve()