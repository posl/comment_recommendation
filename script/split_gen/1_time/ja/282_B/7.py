def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    #oの数を数える
    o_count = [0] * N
    for i in range(N):
        for j in range(M):
            if S[i][j] == 'o':
                o_count[i] += 1
    #oの数が1以上の人を抽出
    o_count_person = []
    for i in range(N):
        if o_count[i] > 0:
            o_count_person.append(i)
    #oの数が1以上の人の組み合わせを出す
    import itertools
    o_count_person_combi = list(itertools.combinations(o_count_person, 2))
    #oの数が1以上の人の組み合わせの中にxが含まれていないものをカウント
    count = 0
    for c in o_count_person_combi:
        x_flag = False
        for i in range(M):
            if S[c[0]][i] == 'x' and S[c[1]][i] == 'x':
                x_flag = True
        if x_flag == False:
            count += 1
    print(count)
