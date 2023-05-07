def main():
    Q = int(input())
    balls = []
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            balls += [int(query[1])] * int(query[2])
        else:
            print(sum(balls[:int(query[1])]))
            balls = balls[int(query[1]):]
