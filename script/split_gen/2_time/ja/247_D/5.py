def main():
    q = int(input())
    x = []
    c = []
    for i in range(q):
        temp = list(map(int, input().split()))
        if temp[0] == 1:
            x.append(temp[1])
            c.append(temp[2])
        elif temp[0] == 2:
            ball = 0
            for j in range(temp[1]):
                ball += x.pop()
            print(ball)
