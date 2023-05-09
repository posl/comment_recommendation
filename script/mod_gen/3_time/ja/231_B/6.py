def main():
    # 入力
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    # 処理
    S_set = set(S)
    S_dict = {}
    for s in S_set:
        S_dict[s] = 0
    for s in S:
        S_dict[s] += 1
    max_vote = 0
    max_vote_name = ""
    for key, value in S_dict.items():
        if value > max_vote:
            max_vote = value
            max_vote_name = key
    # 出力
    print(max_vote_name)

if __name__ == '__main__':
    main()