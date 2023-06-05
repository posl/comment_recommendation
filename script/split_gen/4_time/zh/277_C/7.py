def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1])
    #print(AB)
    ans = 0
    for i in range(N):
        if AB[i][0] <= ans and AB[i][1] > ans:
            ans = AB[i][1]
    print(ans)
main()
