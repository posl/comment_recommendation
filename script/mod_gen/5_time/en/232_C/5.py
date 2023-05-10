def main():
    N, M = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(M)]
    cd = [list(map(int, input().split())) for _ in range(M)]
    for i in range(N):
        for j in range(N):
            if [i+1, j+1] in ab and [i+1, j+1] not in cd:
                print("No")
                exit()
            elif [i+1, j+1] in cd and [i+1, j+1] not in ab:
                print("No")
                exit()
    print("Yes")

if __name__ == '__main__':
    main()