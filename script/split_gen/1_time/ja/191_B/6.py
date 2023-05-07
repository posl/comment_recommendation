def main():
    #入力
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    #A から X と等しい要素を全て取り除き、残った要素をそのままの順序で並べた数列 A' を出力してください。  
    #A から X と等しい要素を全て取り除き、残った要素をそのままの順序で並べた数列 A' を出力してください。  
    for i in A:
        if i == X:
            A.remove(i)
    print(*A)
