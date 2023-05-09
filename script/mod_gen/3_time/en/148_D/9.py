def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A[i] = i + 1 となる i を求める
    # ただし、A[i] = i + 1 となる i が複数ある場合は、
    # A[i] = i + 1 となる最小の i を求める
    # このような i が存在しない場合は、-1 を返す
    def find_i(A, N):
        # A に i + 1 が存在するかどうかを判定する
        def find(A, i):
            if i < 0 or i >= N:
                return False
            return A[i] == i + 1
        # A に i + 1 が存在する場合は、i を返す
        # 存在しない場合は、-1 を返す
        def find_index(A, i):
            if find(A, i):
                return i
            return -1
        # A に i + 1 が存在する場合は、i を返す
        # 存在しない場合は、i - 1 を返す
        def find_index_or_prev(A, i):
            if find(A, i):
                return i
            return i - 1
        # A に i + 1 が存在する場合は、i を返す
        # 存在しない場合は、i + 1 を返す
        def find_index_or_next(A, i):
            if find(A, i):
                return i
            return i + 1
        # A に i + 1 が存在する場合は、i を返す
        # 存在しない場合は、-1 を返す
        # ただし、i が 0 または N - 1 の場合は、
        # それぞれの場合において、A に i + 1 が存在するかどうかを判定する
        def find_index_or

if __name__ == '__main__':
    main()