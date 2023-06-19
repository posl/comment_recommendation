def main():
    n = int(input())
    dic = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s in dic:
            dic[s].append((t, i))
        else:
            dic[s] = [(t, i)]
    for s in dic:
        dic[s].sort(reverse=True)
    max_score = 0
    max_score_idx = 0
    max_score_first_idx = n
    for s in dic:
        if dic[s][0][0] > max_score:
            max_score = dic[s][0][0]
            max_score_idx = dic[s][0][1]
            max_score_first_idx = dic[s][0][1]
        elif dic[s][0][0] == max_score and dic[s][0][1] < max_score_first_idx:
            max_score_first_idx = dic[s][0][1]
            max_score_idx = dic[s][0][1]
    print(max_score_idx + 1)

if __name__ == '__main__':
    main()