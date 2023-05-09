def main():
    Q = int(input())
    #print('Q',Q)
    query_list = []
    for i in range(Q):
        query_list.append(input().split())
    #print('query_list',query_list)
    ball_list = []
    for i in range(Q):
        if query_list[i][0] == '1':
            for j in range(int(query_list[i][2])):
                ball_list.append(query_list[i][1])
        else:
            print(sum([int(ball_list.pop(0)) for i in range(int(query_list[i][1]))]))
    #print('ball_list',ball_list)
