def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(-1)
    ret = [0] * N
    cnt = 1
    for i in range(N):
        if A[i] != A[i+1]:
            ret[cnt-1] += 1
            cnt = 1
        else:
            cnt += 1
    print('\n'.join(map(str, ret)))

if __name__ == '__main__':
    solve()