def solve(n, s, cards):
    # ここに処理を追記
    for i in range(2 ** n):
        sum = 0
        result = ""
        for j in range(n):
            if ((i >> j) & 1):
                sum += cards[j][1]
                result += "T"
            else:
                sum += cards[j][0]
                result += "H"
        if sum == s:
            return "Yes\n" + result
    return "No"
n, s = map(int, input().split())
cards = [list(map(int, input().split())) for i in range(n)]
print(solve(n, s, cards))
