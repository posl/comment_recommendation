def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    B = [list(map(int, input().split())) for _ in range(M)]
    #Aの順列を全列挙
    for p in permutations(range(1, N+1)):
        #Aの順列をBに適用
        Bp = [sorted([p[x-1], p[y-1]]) for x, y in B]
        #AとBpが同じならYes
        if sorted(A) == sorted(Bp):
            print('Yes')
            return
    #全ての順列を試しても一致しなければNo
    print('No')
    return

if __name__ == '__main__':
    main()