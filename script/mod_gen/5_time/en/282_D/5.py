def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    edges.sort(key=lambda x: x[1])
    edges.sort(key=lambda x: x[0])
    print(edges)
    #for i in range(m):
    #    for j in range(i+1, m):
    #        if edges[i][0] < edges[j][0] and edges[i][1] < edges[j][1]:
    #            pass
    #        else:
    #            if edges[i][1] < edges[j][0]:
    #                print(edges[i], edges[j])
    #                ans += 1
    #            elif edges[i][0] > edges[j][1]:
    #                print(edges[i], edges[j])
    #                ans += 1
    #print(ans)

if __name__ == '__main__':
    main()