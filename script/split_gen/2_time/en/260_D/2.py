def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    cards = [0] * N
    for i in range(N):
        cards[i] = i + 1
    for i in range(N):
        cards[P[i] - 1] = i + 1
    print(cards)
    result = [-1] * N
    stack = []
    for i in range(N):
        stack.append(cards[i])
        if len(stack) >= K:
            for j in range(K):
                result[stack.pop() - 1] = i + 1
    for i in range(N):
        print(result[i])
