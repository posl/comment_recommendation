def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        edges.append(list(map(int, input().split())))
    #print(edges)
    #print(len(edges))
    #print(len(set(edges)))
    if len(edges) != len(set(edges)):
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()