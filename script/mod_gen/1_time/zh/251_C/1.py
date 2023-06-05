def judge_best_submission():
    n = int(input())
    s_list = []
    t_list = []
    for i in range(n):
        s, t = input().split(' ')
        s_list.append(s)
        t_list.append(int(t))
    max_t = max(t_list)
    best_s = ''
    for i in range(n):
        if t_list[i] == max_t:
            best_s = s_list[i]
            break
    for i in range(n):
        if s_list[i] == best_s:
            print(i + 1)
            break

if __name__ == '__main__':
    judge_best_submission()