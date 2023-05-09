def main():
    N = int(input())
    jump = []
    for i in range(N):
        x,y,p = map(int,input().split())
        jump.append([x,y,p])
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if jump[i][2] > jump[j][2]:
                tmp = jump[i]
                jump[i] = jump[j]
                jump[j] = tmp
    for i in range(N):
        for j in range(i+1,N):
            if jump[i][2]*ans >= abs(jump[i][0]-jump[j][0]) + abs(jump[i][1]-jump[j][1]):
                continue
            else:
                ans += 1
    print(ans)
