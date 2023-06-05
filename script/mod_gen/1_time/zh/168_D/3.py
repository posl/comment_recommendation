def main():
    N,M = map(int,input().split())
    path = []
    for i in range(M):
        path.append(list(map(int,input().split())))
    print(path)

if __name__ == '__main__':
    main()