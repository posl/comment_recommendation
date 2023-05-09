def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    cards = [0] * N
    for i in range(N):
        cards[i] = P[i] - 1
    eaten = [0] * N
    next = [-1] * N
    stack = [-1] * N
    stack[0] = 0
    top = 0
    for i in range(N):
        next[i] = i + 1
        eaten[i] = -1
    next[N - 1] = -1
    for i in range(N):
        if eaten[cards[i]] != -1:
            continue
        while top >= 0 and cards[stack[top]] < cards[cards[i]]:
            eaten[stack[top]] = i
            top -= 1
        top += 1
        stack[top] = cards[i]
    for i in range(N):
        if eaten[i] == -1:
            eaten[i] = N
    while next[0] != -1:
        top = next[0]
        for i in range(K):
            if top == -1:
                break
            eaten[top] = N
            top = next[top]
        if top != -1:
            next[0] = top
        else:
            next[0] = -1
    for i in range(N):
        print(eaten[i] + 1)
