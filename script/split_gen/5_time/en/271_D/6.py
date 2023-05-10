def solve(N, S, cards):
    for i in range(2**N):
        sum = 0
        for j in range(N):
            if ((i >> j) & 1) == 0:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == S:
            ans = ""
            for j in range(N):
                if ((i >> j) & 1) == 0:
                    ans += "H"
                else:
                    ans += "T"
            return "Yes\n" + ans
    return "No"
