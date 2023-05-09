def main():
    #input
    N, C = map(int, input().split())
    ABC = [[int(i) for i in input().split()] for _ in range(N)]
    ABC.sort(key=lambda x: x[0])
    #compute
    ans = 0
    for i in range(N):
        ans += ABC[i][2]
        ABC[i][1] += 1
    ABC.sort(key=lambda x: x[1])
    for i in range(N):
        ABC[i][0] += 1
    ABC.sort(key=lambda x: x[0])
    #print(ABC)
    for i in range(N):
        if i == 0:
            pass
        elif ABC[i][0] == ABC[i-1][0]:
            ABC[i][2] += ABC[i-1][2]
    #print(ABC)
    for i in range(N):
        if i == 0:
            pass
        elif ABC[i][1] == ABC[i-1][1]:
            ABC[i][2] -= ABC[i-1][2]
    #print(ABC)
    for i in range(N):
        if ABC[i][2] > C:
            ans += C*(ABC[i][1]-ABC[i][0])
        else:
            ans += ABC[i][2]*(ABC[i][1]-ABC[i][0])
    #print(ans)
    #output
    print(ans)
