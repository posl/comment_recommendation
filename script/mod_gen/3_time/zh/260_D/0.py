def eat_cards(cards, k):
    n = len(cards)
    stack = []
    eat = [-1] * n
    for i in range(n):
        while stack and stack[-1][0] < cards[i]:
            _, idx = stack.pop()
            eat[idx] = i + 1
        stack.append((cards[i], i))
        if len(stack) == k:
            stack = []
    return eat

if __name__ == '__main__':
    eat_cards()