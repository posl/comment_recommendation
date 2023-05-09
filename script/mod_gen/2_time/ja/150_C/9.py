def permutation(N, P, Q):
    #N:順列の数
    #P:順列
    #Q:順列
    #P,Qの辞書順の差を返す
    #N = int(input())
    #P = list(map(int, input().split()))
    #Q = list(map(int, input().split()))
    #N = 3
    #P = [1,3,2]
    #Q = [3,1,2]
    #N = 8
    #P = [7,3,5,4,2,1,6,8]
    #Q = [3,8,2,5,4,6,7,1]
    #N = 3
    #P = [1,2,3]
    #Q = [1,2,3]
    #P,Qの辞書順の差を返す
    import itertools
    import bisect
    L = list(itertools.permutations(range(1,N+1)))
    #print(L)
    P = tuple(P)
    Q = tuple(Q)
    #print(P)
    #print(Q)
    a = bisect.bisect_left(L, P)
    b = bisect.bisect_left(L, Q)
    #print(a)
    #print(b)
    return abs(a-b)

if __name__ == '__main__':
    permutation()