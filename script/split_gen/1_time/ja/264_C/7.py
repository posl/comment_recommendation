def main():
    import sys
    input = sys.stdin.readline
    H1,W1 = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H1)]
    H2,W2 = map(int,input().split())
    B = [list(map(int,input().split())) for _ in range(H2)]
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            for h in range(H2):
                for w in range(W2):
                    if A[i+h][j+w] != B[h][w]:
                        break
                else:
                    continue
                break
            else:
                print('Yes')
                return
    print('No')
