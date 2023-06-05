def main():
    Q = int(input())
    query_list = []
    for i in range(Q):
        query_list.append(input().split())
    ball_list = []
    for query in query_list:
        if query[0] == '1':
            for i in range(int(query[2])):
                ball_list.append(query[1])
        else:
            print(sum([int(ball) for ball in ball_list[:int(query[1])]]))
            ball_list = ball_list[int(query[1]):]
