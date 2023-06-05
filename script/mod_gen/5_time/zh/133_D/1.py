def solve():
    N = int(input())
    A = list(map(int,input().split()))
    result = []
    for i in range(N):
        if i%2 == 0:
            result.append(sum(A[0:N:2]))
        else:
            result.append(sum(A[1:N:2]))
    print(' '.join(map(str,result)))

if __name__ == '__main__':
    solve()