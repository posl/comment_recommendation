def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(A)
    print(B)
    A.sort()
    B.sort()
    print(A)
    print(B)
    if A[-1] < B[0]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()