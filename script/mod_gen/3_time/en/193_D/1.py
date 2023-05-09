def main():
    K = int(input())
    S = input()
    T = input()
    cards = [K] * 10
    for n in S:
        cards[int(n)] -= 1
    for n in T:
        cards[int(n)] -= 1
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            taka = S[:-1] + str(i)
            aoki = T[:-1] + str(j)
            if score(taka) > score(aoki):
                if i == j:
                    ans += cards[i] * (cards[i] - 1) / (K * (K - 1))
                else:
                    ans += cards[i] * cards[j] / (K * (K - 1))
    print(ans)

if __name__ == '__main__':
    main()