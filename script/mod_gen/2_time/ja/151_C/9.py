def main():
    n, m = map(int, input().split())
    # 問題数
    problem_count = [0] * n
    # WA数
    wa_count = [0] * n
    # AC数
    ac_count = 0
    # WAのペナルティ数
    wa_penalty = 0
    for i in range(m):
        p, s = input().split()
        p = int(p) - 1
        if s == "AC":
            # 既にAC済みの問題は無視する
            if problem_count[p] == 0:
                ac_count += 1
                wa_penalty += wa_count[p]
        else:
            # WA数を加算
            wa_count[p] += 1
        # 問題数を加算
        problem_count[p] += 1
    print(ac_count, wa_penalty)

if __name__ == '__main__':
    main()