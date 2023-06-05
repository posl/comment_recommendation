def main():
    N, M = map(int, input().split())
    edge = []
    for i in range(M):
        edge.append(list(map(int, input().split())))
    edge.sort()
    v = [0] * N
    for i in range(M):
        v[edge[i][0]-1] += 1
        v[edge[i][1]-1] += 1
    if max(v) == 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()