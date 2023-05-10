def solve(K: int, S: str, T: str):
    card = [K] * 10
    for i in range(4):
        card[int(S[i])] -= 1
        card[int(T[i])] -= 1
    score = 0
    for i in range(1, 10):
        score += i * 10 ** card[i]
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                if card[i] < 2:
                    continue
                else:
                    p = card[i] * (card[i] - 1)
            else:
                if card[i] < 1 or card[j] < 1:
                    continue
                else:
                    p = card[i] * card[j]
            if i == j:
                if score + 2 * 10 ** (card[i] - 2) > score:
                    ans += p / (9 * K - 8) / (9 * K - 9)
            else:
                if score + 10 ** (card[i] - 1) + 10 ** (card[j] - 1) > score:
                    ans += p / (9 * K - 8) / (9 * K - 9)
    return ans

if __name__ == '__main__':
    solve()