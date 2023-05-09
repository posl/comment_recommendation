def main():
    N,M = map(int, input().split())
    kx = [list(map(int, input().split())) for _ in range(M)]
    kx = [[kx[i][j] for j in range(1, kx[i][0]+1)] for i in range(M)]
    #print(kx)
    for i in range(N):
        for j in range(i+1, N):
            if not [i+1, j+1] in kx:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    main()