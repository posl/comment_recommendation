def main():
    # n = int(input())
    # pos = []
    # for i in range(n):
    #     pos.append(list(map(int, input().split())))
    # s = input()
    # pos_x = [0] * n
    # pos_y = [0] * n
    # for i in range(n):
    #     pos_x[i] = pos[i][0]
    #     pos_y[i] = pos[i][1]
    # print(pos_x)
    # print(pos_y)
    # print(s)
    # for i in range(n):
    #     if s[i] == 'L':
    #         pos_x[i] = -pos_x[i]
    #     elif s[i] == 'R':
    #         pos_x[i] = pos_x[i]
    #     else:
    #         print('error')
    # print(pos_x)
    # print(pos_y)
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if pos_x[i] == pos_x[j] and pos_y[i] == pos_y[j]:
    #             print('Yes')
    #             exit()
    # print('No')
    n = int(input())
    pos = []
    for i in range(n):
        pos.append(list(map(int, input().split())))
    s = input()
    pos_x = [0] * n
    pos_y = [0] * n
    for i in range(n):
        pos_x[i] = pos[i][0]
        pos_y[i] = pos[i][1]
    for i in range(n):
        if s[i] == 'L':
            pos_x[i] = -pos_x[i]
        elif s[i] == 'R':
            pos_x[i] = pos_x[i]
        else:
            print('error')
    for i in range(n):
        for j in range(i+1, n):
            if pos_x[i] == pos_x[j] and pos_y[i] == pos_y[j]:
                print('Yes')
                exit()
    print('No')
