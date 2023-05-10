def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append(list(map(int, input().split())))
    q.reverse()
    ans = []
    balls = []
    for i in range(n):
        if q[i][0] == 1:
            balls.append(q[i][1])
        else:
            ans.append(sum(balls[:q[i][1]]))
            balls = balls[q[i][1]:]
    ans.reverse()
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()