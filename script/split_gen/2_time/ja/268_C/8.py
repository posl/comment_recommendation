def main():
    N = int(input())
    p = list(map(int, input().split()))
    # 人 i の目の前にある料理の番号を p_i とする
    # p_i 番目の要素が i であるような配列を作る
    p_inv = [0] * N
    for i in range(N):
        p_inv[p[i]] = i
    # 人 i の目の前にある料理の番号を p_i とすると、
    # p_i 番目の要素が i であるような配列 p_inv に対し、
    # p_inv[i] は i 番目の要素が p_i であることを意味する
    # つまり、p_inv[i] = p_i である
    # 人 i の目の前にある料理の番号を p_i とすると、
    # p_i 番目の要素が i であるような配列 p_inv に対し、
    # p_inv[i] 番目の要素が i であることを意味する
    # つまり、p_inv[p_inv[i]] = i である
    # 人 i の目の前にある料理の番号を p_i とすると、
    # p_i 番目の要素が i であるような配列 p_inv に対し、
    # p_inv[i] 番目の要素が i であることを意味する
    # つまり、p_inv[p_inv[i]] = i である
    # これは、人 i の目の前にある料理の番号を p_i とすると、
    # p_i 番目の要素が i であるような配列 p_inv に対し、
    # p_inv[p_i] 番目の要素が i であることを意味する
    #
