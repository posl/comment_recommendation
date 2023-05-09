def main():
    N = int(input())
    road = [list(map(int, input().split())) for _ in range(N-1)]
    road = [[i+1,road[i][0],road[i][1]] for i in range(N-1)]
    road = sorted(road, key=lambda x: x[1])
    #print(road)
    ans = [1]
    for i in range(N-1):
        if road[i][1] == ans[-1]:
            ans.append(road[i][2])
        elif road[i][2] == ans[-1]:
            ans.append(road[i][1])
        #print(ans)
    ans = ans + ans[::-1]
    print(" ".join(map(str, ans)))
