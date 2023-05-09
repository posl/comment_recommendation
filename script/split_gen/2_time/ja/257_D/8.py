def main():
    N = int(input())
    jump = []
    for i in range(N):
        jump.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if jump[i][2] * ans < abs(jump[i][0] - jump[j][0]) + abs(jump[i][1] - jump[j][1]):
                ans = (abs(jump[i][0] - jump[j][0]) + abs(jump[i][1] - jump[j][1])) // jump[i][2] + 1
    print(ans)
