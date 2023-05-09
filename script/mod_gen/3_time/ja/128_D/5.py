def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(N,K)+1):
        for r in range(min(N,K)-l+1):
            hand = V[:l] + V[N-r:]
            hand.sort()
            for i in range(K-l-r):
                if hand and hand[0] < 0:
                    hand.pop(0)
                else:
                    break
            ans = max(ans, sum(hand))
    print(ans)

if __name__ == '__main__':
    main()