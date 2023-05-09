def main():
    N = int(input())
    P = list(map(int,input().split()))
    Q = list(map(int,input().split()))
    #N!通りの順列を作成
    import itertools
    a = list(itertools.permutations(range(1,N+1),N))
    #a.index(P)は、Pがaの何番目かを返す
    print(abs(a.index(tuple(P))-a.index(tuple(Q))))

if __name__ == '__main__':
    main()