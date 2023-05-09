def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    #Aを昇順にソート
    A.sort()
    
    #Bを昇順にソート
    B.sort()
    
    #Aの各要素とBの各要素の差を計算する
    #差の絶対値の最小値を出力する
    print(min([abs(a - b) for a in A for b in B]))
