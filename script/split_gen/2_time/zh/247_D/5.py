def main():
    q = int(input())
    data = []
    for i in range(q):
        data.append(input().split())
    for i in range(q):
        if data[i][0] == '1':
            data[i][1] = int(data[i][1])
            data[i][2] = int(data[i][2])
            if i == 0:
                ball = [data[i][1]]*data[i][2]
            else:
                ball = ball + [data[i][1]]*data[i][2]
        else:
            data[i][1] = int(data[i][1])
            if i == 0:
                print(sum(ball[:data[i][1]]))
                ball = ball[data[i][1]:]
            else:
                print(sum(ball[:data[i][1]]))
                ball = ball[data[i][1]:]
