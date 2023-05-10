def solve():
    N = int(input())
    A = list(map(int,input().split()))
    a = set()
    for i in range(4*N-1):
        if A[i] in a:
            a.remove(A[i])
        else:
            a.add(A[i])
    print(a.pop())

if __name__ == '__main__':
    solve()