def main():
    N,X,Y = map(int,input().split())
    edge = []
    for i in range(N-1):
        edge.append(list(map(int,input().split())))
    print(edge)

if __name__ == '__main__':
    main()