def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    #内積
    inner_product = 0
    for i in range(N):
        inner_product += A[i]*B[i]
    
    #出力
    if inner_product == 0:
        print('Yes')
    else:
        print('No')
