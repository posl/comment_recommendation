def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(input().split())
    L = [int(L[i][0]) for i in range(N)]
    print(len(set(L)))

if __name__ == '__main__':
    main()