def main():
    N = int(input())
    town = []
    for i in range(N):
        town.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(N):
            ans += ((town[j][0]-town[i][0])**2+(town[j][1]-town[i][1])**2)**0.5
    print(ans/N)
