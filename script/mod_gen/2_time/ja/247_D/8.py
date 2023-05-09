def main():
    Q = int(input())
    query = [list(map(int,input().split())) for _ in range(Q)]
    balls = []
    for q in query:
        if q[0]==1:
            balls += [q[1]]*q[2]
        else:
            print(sum(balls[:q[1]]))
            balls = balls[q[1]:]
main()

if __name__ == '__main__':
    main()