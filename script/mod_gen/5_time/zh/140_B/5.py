def sum_score(a,b,c):
    score = 0
    for i in range(len(a)):
        score += b[a[i]-1]
        if i < len(a)-1:
            if a[i+1] == a[i] + 1:
                score += c[a[i]-1]
    return score

if __name__ == '__main__':
    sum_score()