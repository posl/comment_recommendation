def dfs(town,visited,dis):
    if len(visited) == N:
        dis += ((town[0]-visited[0][0])**2+(town[1]-visited[0][1])**2)**0.5
        return dis
    else:
        for i in range(N):
            if i not in visited:
                dis += ((town[0]-towns[i][0])**2+(town[1]-towns[i][1])**2)**0.5
                visited.append(i)
                dfs(towns[i],visited,dis)
                visited.pop()
                dis -= ((town[0]-towns[i][0])**2+(town[1]-towns[i][1])**2)**0.5
N = int(input())
towns = [list(map(int,input().split())) for i in range(N)]
visited = [0]
dis = 0
dfs(towns[0],visited,dis)
print(dis)
I am trying to calculate the average length of all the possible paths in a graph. I have written a recursive function that will calculate the length of all the paths, but I am having trouble calculating the average. I have tried to calculate the average by multiplying the total length of all the paths by a factor of 1/N! and that does not seem to be working. I am not sure why. Any help would be appreciated.
I am trying to make a program that will calculate the average length of all the possible paths in a graph. I have written a recursive function that will calculate the length of all the paths, but I am having trouble calculating the average. I have tried to calculate the average by multiplying the total length of all the paths by a factor of 1/N! and that does not seem to be working. I am not sure why. Any help would be appreciated.

if __name__ == '__main__':
    dfs()