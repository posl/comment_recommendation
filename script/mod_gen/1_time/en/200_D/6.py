def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A_i mod 200
    mod = [a % 200 for a in A]
    # A_i mod 200の値に対応するindexを格納
    mod_index = [[] for _ in range(200)]
    for i in range(N):
        mod_index[mod[i]].append(i+1)
    # mod_index[i]の要素数が2以上であれば、それらの要素の和が200の倍数である
    for i in range(200):
        if len(mod_index[i]) >= 2:
            print('Yes')
            print(1, mod_index[i][0])
            print(len(mod_index[i])-1, *mod_index[i][1:])
            return
    print('No')

if __name__ == '__main__':
    main()