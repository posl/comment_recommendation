def main():
    # Take input Here and Call solution function
    m = int(input())
    graph = []
    for i in range(m):
        x,y = map(int,input().split())
        graph.append([x,y])
    pieces = list(map(int,input().split()))
    print(solution(m,graph,pieces))
