def bingo():
    n = 3
    bingo = []
    for i in range(n):
        bingo.append(list(map(int, input().split())))
    m = int(input())
    nums = []
    for i in range(m):
        nums.append(int(input()))
    for i in range(n):
        for j in range(n):
            if bingo[i][j] in nums:
                bingo[i][j] = 0
    for i in range(n):
        if sum(bingo[i]) == 0:
            return "Yes"
    for i in range(n):
        if bingo[0][i] + bingo[1][i] + bingo[2][i] == 0:
            return "Yes"
    if bingo[0][0] + bingo[1][1] + bingo[2][2] == 0:
        return "Yes"
    if bingo[0][2] + bingo[1][1] + bingo[2][0] == 0:
        return "Yes"
    return "No"
print(bingo())
