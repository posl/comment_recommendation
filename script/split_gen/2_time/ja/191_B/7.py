def main():
    #入力
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    #処理
    #AからXと等しい要素を全て取り除き、残った要素をそのままの順序で並べた数列 A' を出力してください。
    #A'の要素を空白区切りで順に出力せよ。
    #A' が要素数 0 の数列となる場合があります。この場合、空行を出力するだけで構いません。
    A = [a for a in A if a != X]
    print(*A)
