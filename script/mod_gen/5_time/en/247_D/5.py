def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append(input().split())
    balls = []
    for i in range(n):
        if q[i][0] == '1':
            for j in range(int(q[i][2])):
                balls.append(int(q[i][1]))
        else:
            print(sum(balls[:int(q[i][1])]))
            del balls[:int(q[i][1])]
    return 0

if __name__ == '__main__':
    main()