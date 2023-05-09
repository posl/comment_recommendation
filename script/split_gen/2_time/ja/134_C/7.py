def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    #Aを降順にソート
    A.sort(reverse=True)
    #Aの最大値を求める
    max_A = A[0]
    #Aの2番目の最大値を求める
    second_max_A = A[1]
    
    for i in range(N):
        if A[i] == max_A:
            print(second_max_A)
        else:
            print(max_A)
