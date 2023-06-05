def main():
    n = int(input())
    scores = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s not in scores:
            scores[s] = t
        else:
            scores[s] += t
    max_score = 0
    max_score_s = ""
    for s in scores:
        if scores[s] > max_score:
            max_score = scores[s]
            max_score_s = s
    print(max_score_s)

if __name__ == '__main__':
    main()