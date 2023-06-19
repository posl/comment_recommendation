def bingo():
    row1 = [int(i) for i in input().split()]
    row2 = [int(i) for i in input().split()]
    row3 = [int(i) for i in input().split()]
    N = int(input())
    b = []
    for i in range(N):
        b.append(int(input()))
    flag = False
    for i in range(3):
        if row1[i] in b and row2[i] in b and row3[i] in b:
            flag = True
            break
    for i in range(3):
        if row1[i] in b and row2[i] in b and row3[i] in b:
            flag = True
            break
    if row1[0] in b and row2[1] in b and row3[2] in b:
        flag = True
    if row1[2] in b and row2[1] in b and row3[0] in b:
        flag = True
    if flag:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    bingo()