def main():
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H)]
    sum_A = sum([sum(A[i]) for i in range(H)])
    min_A = min([min(A[i]) for i in range(H)])
    print(sum_A - min_A*H*W)
main()
