def main():
    Q = int(input())
    balls = []
    total = 0
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            balls.append(int(query[1]))
            total += int(query[2])
        else:
            print(total)
            total -= balls.pop(0)
    return
