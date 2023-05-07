def bingo():
    bingo_card = []
    for i in range(3):
        bingo_card.append(list(map(int, input().split())))
    N = int(input())
    b = []
    for i in range(N):
        b.append(int(input()))
    bingo_list = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            if bingo_card[i][j] in b:
                bingo_list[i][j] = 1
    bingo = False
    for i in range(3):
        if bingo_list[i][0] == 1 and bingo_list[i][1] == 1 and bingo_list[i][2] == 1:
            bingo = True
        if bingo_list[0][i] == 1 and bingo_list[1][i] == 1 and bingo_list[2][i] == 1:
            bingo = True
    if bingo_list[0][0] == 1 and bingo_list[1][1] == 1 and bingo_list[2][2] == 1:
        bingo = True
    if bingo_list[0][2] == 1 and bingo_list[1][1] == 1 and bingo_list[2][0] == 1:
        bingo = True
    if bingo:
        print("Yes")
    else:
        print("No")
bingo()
I have a problem with the following code: I want to get the value of the key "name" of the dictionary "person" and put it in the variable "name" of the function "print_name". I don't know how to do it. I've tried many things but I can't get it to work.
person = {"name": "John", "age": 36, "country": "Norway"}
