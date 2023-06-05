def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    #print(n, k, p, c)
    max_score = -1e9
    for i in range(n):
        score = 0
        j = i
        step = 0
        while True:
            j = p[j] - 1
            score += c[j]
            step += 1
            if j == i:
                break
            if step == k:
                break
        if step < k and score > 0:
            score += (k - step) // step * score
        if score > max_score:
            max_score = score
    print(max_score)
