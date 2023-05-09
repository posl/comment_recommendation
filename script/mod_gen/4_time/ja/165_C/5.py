def calc_score(arr, N, Q):
    score = 0
    for i in range(Q):
        a = arr[i][0]
        b = arr[i][1]
        c = arr[i][2]
        d = arr[i][3]
        if arr[b-1] - arr[a-1] == c:
            score += d
    return score

if __name__ == '__main__':
    calc_score()