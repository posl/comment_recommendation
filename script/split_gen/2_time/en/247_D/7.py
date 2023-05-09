def main():
    q = int(input())
    balls = {}
    ball_num = 0
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            balls[ball_num] = [query[1], query[2]]
            ball_num += 1
        else:
            count = query[1]
            sum = 0
            for i in range(ball_num):
                sum += balls[i][0]
                count -= 1
                if count == 0:
                    break
            print(sum)
            ball_num -= query[1]
