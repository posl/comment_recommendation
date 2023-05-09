def main():
    #数列の長さ
    N = 3
    #数列を格納する配列
    A = [0]*N
    #数列の要素を格納
    for i in range(N):
        A[i] = int(input())
    #等差数列にできるか判定
    if (A[1]-A[0]) == (A[2]-A[1]):
        print("Yes")
    else:
        print("No")
