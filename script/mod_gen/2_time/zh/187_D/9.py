def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort(reverse=True)
    B.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += A[i]
        ans -= B[i]
        if ans < 0:
            print(i+1)
            return
    print(N)
    return

if __name__ == '__main__':
    solve()