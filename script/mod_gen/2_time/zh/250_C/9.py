def func1():
    N, Q = map(int, input().split())
    ball = [i+1 for i in range(N)]
    #print(ball)
    for i in range(Q):
        x = int(input())
        #print(x)
        index = ball.index(x)
        #print(index)
        if index != N-1:
            ball[index], ball[index+1] = ball[index+1], ball[index]
        else:
            ball[index], ball[0] = ball[0], ball[index]
        #print(ball)
    print(*ball)

if __name__ == '__main__':
    func1()