def solve():
    q = int(input())
    query = [input().split() for _ in range(q)]
    query = [(int(q[0]), int(q[1]), int(q[2])) for q in query]
    query = [(q[0], q[1], q[2]) if q[0] == 1 else (q[0], q[1], 0) for q in query]
    balls = []
    sum = 0
    for q in query:
        if q[0] == 1:
            for i in range(q[2]):
                balls.append(q[1])
                sum += q[1]
        else:
            for i in range(q[1]):
                sum -= balls[i]
            balls = balls[q[1]:]
            print(sum)

if __name__ == '__main__':
    solve()