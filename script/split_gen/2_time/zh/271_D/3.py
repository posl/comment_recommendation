def solve(n, s, cards):
    for i in range(2 ** n):
        visible = [0] * n
        for j in range(n):
            if i >> j & 1:
                visible[j] = 1
        sum = 0
        for j in range(n):
            if visible[j]:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == s:
            print("Yes")
            for j in range(n):
                if visible[j]:
                    print("H", end="")
                else:
                    print("T", end="")
            print()
            return
    print("No")
