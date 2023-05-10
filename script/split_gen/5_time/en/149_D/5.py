def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    t = list(t)
    score = 0
    for i in range(n):
        if i >= k and t[i] == t[i-k] and t[i-k] != "x":
            t[i] = "x"
        else:
            if t[i] == "r":
                score += p
            elif t[i] == "s":
                score += r
            elif t[i] == "p":
                score += s
    print(score)
