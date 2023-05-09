def main():
    N = int(input())
    que = []
    for i in range(N):
        que.append(input())
    que = que[::-1]
    #print(que)
    ball = []
    add = 0
    while(que):
        q = que.pop()
        q = q.split()
        #print(q)
        if q[0] == "1":
            ball.append(int(q[1]) - add)
        elif q[0] == "2":
            add += int(q[1])
        else:
            min_ball = min(ball)
            print(min_ball + add)
            ball.remove(min_ball)
