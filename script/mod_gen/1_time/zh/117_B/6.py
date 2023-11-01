def judge_polygon(N, L):
    if max(L) < sum(L) - max(L):
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    judge_polygon()