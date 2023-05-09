def main():
    N, M = map(int, input().split())
    if M != N-1:
        print("No")
        return
    edges = []
    for _ in range(M):
        edges.append(list(map(int, input().split())))
    if len(edges) != len(set([tuple(edge) for edge in edges])):
        print("No")
        return
    if len(set([edge[0] for edge in edges])) > 1 and len(set([edge[1] for edge in edges])) > 1:
        print("No")
        return
    print("Yes")
    return

if __name__ == '__main__':
    main()