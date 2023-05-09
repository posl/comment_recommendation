def swap(i):
    global ball
    tmp = ball[i]
    ball[i] = ball[i + 1]
    ball[i + 1] = tmp
n, q = map(int, input().split())
ball = [i + 1 for i in range(n)]
for i in range(q):
    x = int(input())
    for j in range(n):
        if ball[j] == x:
            swap(j)
            break
    print(' '.join(map(str, ball)))
