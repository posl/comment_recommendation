Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    #读取数据
    A = []
    for i in range(3):
        A.append(list(map(int, input().split())))
    N = int(input())
    b = []
    for i in range(N):
        b.append(int(input()))
    #判断是否有宾果
    for i in range(3):
        for j in range(3):
            if A[i][j] in b:
                A[i][j] = 0
    for i in range(3):
        if A[i][0] == A[i][1] == A[i][2] == 0:
            print('Yes')
            exit()
    for i in range(3):
        if A[0][i] == A[1][i] == A[2][i] == 0:
            print('Yes')
            exit()
    if A[0][0] == A[1][1] == A[2][2] == 0:
        print('Yes')
        exit()
    if A[0][2] == A[1][1] == A[2][0] == 0:
        print('Yes')
        exit()
    print('No')
    return

=======
Suggestion 2

def main():
    bingo = [[],[],[]]
    for i in range(3):
        bingo[i] = list(map(int, input().split()))
    N = int(input())
    b = []
    for i in range(N):
        b.append(int(input()))
    for i in range(3):
        for j in range(3):
            for k in range(N):
                if bingo[i][j] == b[k]:
                    bingo[i][j] = 0
    ans = 'No'
    for i in range(3):
        if bingo[i][0] == 0 and bingo[i][1] == 0 and bingo[i][2] == 0:
            ans = 'Yes'
        if bingo[0][i] == 0 and bingo[1][i] == 0 and bingo[2][i] == 0:
            ans = 'Yes'
    if bingo[0][0] == 0 and bingo[1][1] == 0 and bingo[2][2] == 0:
        ans = 'Yes'
    if bingo[0][2] == 0 and bingo[1][1] == 0 and bingo[2][0] == 0:
        ans = 'Yes'
    print(ans)

=======
Suggestion 3

def main():
    bingo = []
    for i in range(3):
        bingo.append(list(map(int, input().split())))
    n = int(input())
    b = []
    for i in range(n):
        b.append(int(input()))
    flag = False
    for i in range(3):
        if bingo[i][0] in b and bingo[i][1] in b and bingo[i][2] in b:
            flag = True
    for i in range(3):
        if bingo[0][i] in b and bingo[1][i] in b and bingo[2][i] in b:
            flag = True
    if bingo[0][0] in b and bingo[1][1] in b and bingo[2][2] in b:
        flag = True
    if bingo[0][2] in b and bingo[1][1] in b and bingo[2][0] in b:
        flag = True
    if flag:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    bingo = []
    for i in range(3):
        bingo.append(list(map(int, input().split())))

    N = int(input())
    for i in range(N):
        b = int(input())
        for j in range(3):
            for k in range(3):
                if bingo[j][k] == b:
                    bingo[j][k] = 0

    for i in range(3):
        if bingo[i][0] == bingo[i][1] == bingo[i][2] == 0:
            print("Yes")
            exit()
        if bingo[0][i] == bingo[1][i] == bingo[2][i] == 0:
            print("Yes")
            exit()

    if bingo[0][0] == bingo[1][1] == bingo[2][2] == 0:
        print("Yes")
        exit()
    if bingo[0][2] == bingo[1][1] == bingo[2][0] == 0:
        print("Yes")
        exit()

    print("No")

=======
Suggestion 5

def main():
    # 读入数据
    matrix = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        matrix[i] = list(map(int, input().split()))
    n = int(input())
    b = [0 for i in range(n)]
    for i in range(n):
        b[i] = int(input())

    # 处理数据
    for i in range(3):
        for j in range(3):
            for k in range(n):
                if matrix[i][j] == b[k]:
                    matrix[i][j] = 0
                    break

    # 判断是否有宾果
    bingo = False
    for i in range(3):
        if matrix[i][0] == 0 and matrix[i][1] == 0 and matrix[i][2] == 0:
            bingo = True
            break
        if matrix[0][i] == 0 and matrix[1][i] == 0 and matrix[2][i] == 0:
            bingo = True
            break
    if matrix[0][0] == 0 and matrix[1][1] == 0 and matrix[2][2] == 0:
        bingo = True
    if matrix[0][2] == 0 and matrix[1][1] == 0 and matrix[2][0] == 0:
        bingo = True

    # 输出结果
    if bingo:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 6

def bingo():
    # 读取输入
    A = []
    for i in range(3):
        A.append(list(map(int, input().split())))
    N = int(input())
    b = []
    for i in range(N):
        b.append(int(input()))

    # 算法
    # 横向
    for i in range(3):
        if A[i][0] in b and A[i][1] in b and A[i][2] in b:
            return 'Yes'
    # 纵向
    for i in range(3):
        if A[0][i] in b and A[1][i] in b and A[2][i] in b:
            return 'Yes'
    # 斜向
    if A[0][0] in b and A[1][1] in b and A[2][2] in b:
        return 'Yes'
    if A[0][2] in b and A[1][1] in b and A[2][0] in b:
        return 'Yes'
    # 其他
    return 'No'

print(bingo())

=======
Suggestion 7

def bingo():
    bingo_map = []
    for i in range(3):
        bingo_map.append(list(map(int, input().split())))
    bingo_num = int(input())
    bingo_list = []
    for i in range(bingo_num):
        bingo_list.append(int(input()))
    for i in range(3):
        for j in range(3):
            if bingo_map[i][j] in bingo_list:
                bingo_map[i][j] = 0
    #print(bingo_map)
    if bingo_map[0][0] == bingo_map[0][1] == bingo_map[0][2] == 0:
        print('Yes')
        return
    if bingo_map[1][0] == bingo_map[1][1] == bingo_map[1][2] == 0:
        print('Yes')
        return
    if bingo_map[2][0] == bingo_map[2][1] == bingo_map[2][2] == 0:
        print('Yes')
        return
    if bingo_map[0][0] == bingo_map[1][0] == bingo_map[2][0] == 0:
        print('Yes')
        return
    if bingo_map[0][1] == bingo_map[1][1] == bingo_map[2][1] == 0:
        print('Yes')
        return
    if bingo_map[0][2] == bingo_map[1][2] == bingo_map[2][2] == 0:
        print('Yes')
        return
    if bingo_map[0][0] == bingo_map[1][1] == bingo_map[2][2] == 0:
        print('Yes')
        return
    if bingo_map[0][2] == bingo_map[1][1] == bingo_map[2][0] == 0:
        print('Yes')
        return
    print('No')
    return

bingo()

=======
Suggestion 8

def bingo(bingo_card, bingo_num):
    bingo_line = [[bingo_card[0][0], bingo_card[0][1], bingo_card[0][2]],
                  [bingo_card[1][0], bingo_card[1][1], bingo_card[1][2]],
                  [bingo_card[2][0], bingo_card[2][1], bingo_card[2][2]],
                  [bingo_card[0][0], bingo_card[1][0], bingo_card[2][0]],
                  [bingo_card[0][1], bingo_card[1][1], bingo_card[2][1]],
                  [bingo_card[0][2], bingo_card[1][2], bingo_card[2][2]],
                  [bingo_card[0][0], bingo_card[1][1], bingo_card[2][2]],
                  [bingo_card[0][2], bingo_card[1][1], bingo_card[2][0]]]
    for i in range(len(bingo_line)):
        if set(bingo_line[i]) & set(bingo_num) == set(bingo_line[i]):
            return 'Yes'
    return 'No'

=======
Suggestion 9

def main():
    matrix = []
    for i in range(3):
        matrix.append(list(map(int, input().split())))
    N = int(input())
    bingo = []
    for i in range(N):
        bingo.append(int(input()))
    flag = 0
    for i in range(3):
        if matrix[0][i] in bingo and matrix[1][i] in bingo and matrix[2][i] in bingo:
            flag = 1
            break
    for i in range(3):
        if matrix[i][0] in bingo and matrix[i][1] in bingo and matrix[i][2] in bingo:
            flag = 1
            break
    if matrix[0][0] in bingo and matrix[1][1] in bingo and matrix[2][2] in bingo:
        flag = 1
    if matrix[0][2] in bingo and matrix[1][1] in bingo and matrix[2][0] in bingo:
        flag = 1
    if flag == 1:
        print("Yes")
    else:
        print("No")
main()

=======
Suggestion 10

def bingo():
    #输入数据
    matrix = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        matrix[i] = list(map(int,input().split()))
    n = int(input())
    b = [0]*n
    for i in range(n):
        b[i] = int(input())
    #判断
    for i in range(3):
        if matrix[i][0] in b and matrix[i][1] in b and matrix[i][2] in b:
            return "Yes"
    for i in range(3):
        if matrix[0][i] in b and matrix[1][i] in b and matrix[2][i] in b:
            return "Yes"
    if matrix[0][0] in b and matrix[1][1] in b and matrix[2][2] in b:
        return "Yes"
    if matrix[0][2] in b and matrix[1][1] in b and matrix[2][0] in b:
        return "Yes"
    return "No"
