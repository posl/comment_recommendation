def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    C = [i-1 for i in C]
    D = {}
    for i in C:
        if i in D:
            D[i] += 1
        else:
            D[i] = 1
    ans = 0
    for i in range(N):
        if B[i] in D:
            ans += D[B[i]]
    print(ans)

if __name__ == '__main__':
    solve()