def main():
    A = [list(map(int, input().split())) for _ in range(3)]
    N = int(input())
    B = [int(input()) for _ in range(N)]
    
    bingo = False
    for i in range(3):
        if all(A[i][j] in B for j in range(3)):
            bingo = True
            break
        if all(A[j][i] in B for j in range(3)):
            bingo = True
            break
    if all(A[i][i] in B for i in range(3)):
        bingo = True
    if all(A[i][2-i] in B for i in range(3)):
        bingo = True
        
    if bingo:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()