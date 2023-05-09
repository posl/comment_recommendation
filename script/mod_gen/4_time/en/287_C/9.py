def path_graph():
    n,m = map(int, input().split())
    edge = []
    for i in range(m):
        edge.append(list(map(int, input().split())))
    edge.sort()
    for i in range(1, n):
        if [i, i+1] not in edge:
            return "No"
    return "Yes"
print(path_graph())

if __name__ == '__main__':
    path_graph()