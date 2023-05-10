def solve():
    N, S = map(int, input().split())
    cards = []
    for i in range(N):
        a, b = map(int, input().split())
        cards.append((a, b))
    for i in range(2**N):
        sum = 0
        for j in range(N):
            if (i >> j) & 1:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == S:
            ans = ""
            for j in range(N):
                if (i >> j) & 1:
                    ans += "H"
                else:
                    ans += "T"
            print("Yes")
            print(ans)
            return
    print("No")
