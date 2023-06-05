def max_score(n, k, p, c):
    max_score = -1000000000
    for i in range(n):
        score = 0
        step = 0
        next = i
        while step < k:
            next = p[next] - 1
            score += c[next]
            if score > max_score:
                max_score = score
            step += 1
            if next == i:
                break
    return max_score

if __name__ == '__main__':
    max_score()