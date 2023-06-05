def main():
    n = int(input())
    scores = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s not in scores:
            scores[s] = [t, i]
        else:
            if scores[s][0] < t:
                scores[s] = [t, i]
    max_score = 0
    max_score_index = 0
    for key in scores:
        if scores[key][0] > max_score:
            max_score = scores[key][0]
            max_score_index = scores[key][1]
    print(max_score_index + 1)

if __name__ == '__main__':
    main()