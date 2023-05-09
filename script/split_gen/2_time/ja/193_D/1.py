def main():
    K = int(input())
    S = input()
    T = input()
    card = [K] * 9
    for i in range(4):
        card[int(S[i]) - 1] -= 1
        card[int(T[i]) - 1] -= 1
    cnt = 0
    for i in range(9):
        for j in range(9):
            if i == j:
                if card[i] < 2:
                    continue
            else:
                if card[i] < 1 or card[j] < 1:
                    continue
            s = [int(S[0]), int(S[1]), int(S[2]), int(S[3]), i + 1]
            t = [int(T[0]), int(T[1]), int(T[2]), int(T[3]), j + 1]
            s.sort(reverse=True)
            t.sort(reverse=True)
            if sum(s[:4]) > sum(t[:4]):
                if i == j:
                    cnt += card[i] * (card[i] - 1)
                else:
                    cnt += card[i] * card[j]
    print(cnt / (9 * K - 8) / (9 * K - 9))
