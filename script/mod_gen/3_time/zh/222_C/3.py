def playGame(a, b):
    if a == 'G':
        if b == 'G':
            return 0
        elif b == 'C':
            return 1
        elif b == 'P':
            return -1
    elif a == 'C':
        if b == 'G':
            return -1
        elif b == 'C':
            return 0
        elif b == 'P':
            return 1
    elif a == 'P':
        if b == 'G':
            return 1
        elif b == 'C':
            return -1
        elif b == 'P':
            return 0
n, m = map(int, input().split())
a = []
for i in range(2*n):
    a.append(input())
win = []
for i in range(2*n):
    win.append([0, i+1])
for i in range(m):
    for j in range(n):
        result = playGame(a[win[j*2][1]-1][i], a[win[j*2+1][1]-1][i])
        if result == 1:
            win[j*2][0] += 1
        elif result == -1:
            win[j*2+1][0] += 1
    win.sort(reverse=True)
for i in range(2*n):
    print(win[i][1])

if __name__ == '__main__':
    playGame()