def move(i):
    global P
    for j in range(4):
        if j + A[i] < 4:
            if field[j + A[i]] > 0:
                field[j + A[i]] += field[j]
            else:
                field[j + A[i]] = field[j]
        else:
            P += field[j]
N = int(input())
A = list(map(int, input().split()))
field = [0] * 4
P = 0
for i in range(N):
    field[0] += 1
    move(i)
print(P)

if __name__ == '__main__':
    move()